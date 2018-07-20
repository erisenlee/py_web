from .database import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    def __init__(self, name, password, email=None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))

    def __repr__(self):
        return '<User %r>' % (self.name)

class UploadFile(db.Model):


    def __init__(self,filename):
        self.filename=filename


    id=db.Column(db.Integer(),primary_key=True)
    filename=db.Column(db.String(255))
    upload_date=db.Column(db.DateTime())

