import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE_HOST = os.environ.get('DATABASE_HOST_FLASK'),
        DATABASE = os.environ.get('DATABASE_FLASK'),
        DATABASE_USER = os.environ.get('DATABASE_USER_FLASK'),
        DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD_FLASK')
    )

    from . import db
    db.init_app(app)

    from . import controller
    app.register_blueprint(controller.bp)

    return app