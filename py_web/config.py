import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class Config:
    pass


class DevConfig(Config):
    DEBUG=True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI='mysql://root:1234@127.0.0.1:3306/py_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    UPLOAD_FOLDER=os.path.join(BASE_DIR,'uploads')

class ProConfig(Config):
    pass