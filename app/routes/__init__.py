from .main import main_bp
from .login import auth_login_bp
from .register import auth_register_bp


def init_routes(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_login_bp, url_prefix="/auth")
    app.register_blueprint(auth_register_bp, url_prefix="/auth")
