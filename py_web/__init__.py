from flask import Flask

from .database import db
from py_web.controllers.auth import auth
from py_web.controllers.upload import upload


def create_app(Config_obj):
    app=Flask(__name__)

    app.config.from_object(Config_obj)

    db.init_app(app)

    app.register_blueprint(auth)
    app.register_blueprint(upload)






    return app