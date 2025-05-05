from flask import Flask
from extensions import db
from config import Config
from routes import init_routes

# from models import User, Account


def create_app():
    app = Flask(__name__)
    init_routes(app)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
