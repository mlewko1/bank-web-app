from flask import Flask
from flask_login import LoginManager
from .extensions import db
from .config import Config
from .models.user import User  # Dodaj ten import


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicjalizacja rozszerzeń
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Konfiguracja user_loader - KLUCZOWA ZMIANA
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Rejestracja blueprintów
    from .routes import init_routes

    init_routes(app)

    # Utwórz tabele w bazie danych
    with app.app_context():
        db.create_all()

    return app
