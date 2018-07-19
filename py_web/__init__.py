from flask import Flask

from .database import db
from py_web.controllers.auth import auth


def create_app(Config_obj):
    app=Flask(__name__)

    app.config.from_object(Config_obj)

    db.init_app(app)

    app.register_blueprint(auth)






    return app