from .database import db
from py_web.ext import bcrypt


class User(db.Model):
    # __tablename__ = 't_user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user', lazy='dynamic')

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def __str__(self, username):
        self.username = username

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % (self.name)

tags = db.Table('post_tags',
                db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True))


class Post(db.Model):
    # __tablename__ = 't_post'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text())
    pub_date = db.Column(db.DateTime())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic')
    tags = db.relationship('Tag', secondary=tags, backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return "<Post '{}'>".format(self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return "<Tag '{}'>".format(self.title)


class Comment(db.Model):
    # __tablename__ = 't_comment'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __str__(self):
        return "<Comment '{}'>".format(self.text[:5])

class UploadFile(db.Model):


    def __init__(self,filename):
        self.filename=filename


    id=db.Column(db.Integer(),primary_key=True)
    filename=db.Column(db.String(255))
    upload_date=db.Column(db.DateTime())

