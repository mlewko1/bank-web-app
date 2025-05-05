from .main import main_bp


def init_routes(app):
    app.register_blueprint(main_bp)
