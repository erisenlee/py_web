from flask import Flask

from .database import db
from py_web.controllers.auth import auth
from py_web.controllers.upload import upload
from py_web.controllers.blog import blog
from py_web.ext import bcrypt, file
from flask_uploads import configure_uploads
from flask import redirect,url_for

def create_app(Config_obj):
    app = Flask(__name__)

    app.config.from_object(Config_obj)

    db.init_app(app)
    bcrypt.init_app(app)
    configure_uploads(app, (file,))

    @app.route('/')
    def index():
        return redirect(url_for('blog.blog_home'))
    app.register_blueprint(blog)
    app.register_blueprint(auth)
    app.register_blueprint(upload)



    return app
