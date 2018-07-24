from flask import (Blueprint, flash, redirect, render_template, request, session, url_for, g)
from functools import wraps
from py_web.database import db
from py_web.models import User
from py_web.forms import RegistrationForm,LoginForm

auth = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@auth.route('/register', methods=('GET', 'POST'))
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash('User {} is already registered.'.format(form.username.data),category='danger')
        user=User(username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering!Please login.',category='Success')
        return redirect(url_for('auth/login'))
    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=('GET', 'POST'))
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        error=None
        if user is None:
            error='Incorrect username.'
        elif not user.check_password(form.password.data):
            error='Incorrect password.'
        if error is None:
            session.clear()
            session['user_id']=user.id
            # flash('Login success!',category='success')
            return redirect(url_for('auth.index'))
        flash(error, category='danger')

    return render_template('auth/login.html', form=form)



@auth.route('/',methods=['GET','POST'])
def index():
    form=LoginForm()
    if request.method=='POST' and form.validate():
        if form.username.data:
            flash('dsafasdsdf',category='info')
            # redirect(url_for('auth.index'))
    # flash('dsdsds',category='info')
    return render_template('upload/test_form.html',form=form)