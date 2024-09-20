from flask import Flask

def create_app():
    app = Flask(__name__)

    from .main_routes import (main_bp)
    app.register_blueprint(main_bp)

    from .user_routes import (user_bp)
    app.register_blueprint(user_bp, url_prefix='/profile')
    return app