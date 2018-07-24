import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class Config:
    pass


class DevConfig(Config):
    DEBUG=True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI='mysql://root:1234@127.0.0.1:3306/py_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    UPLOADED_FILES_DEST=os.path.join(BASE_DIR,'uploads/files')
    # UPLOADED_FILES_ALLOW = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx', 'csv']


class ProConfig(Config):
    pass