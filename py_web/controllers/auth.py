from flask import (Blueprint, flash, redirect, render_template, request, session, url_for, g)
from functools import wraps
from py_web.database import db
from py_web.models import User
from py_web.forms import RegistrationForm
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
    form=RegistrationForm(request.form)
    if request.method=='POST' and form.validate():
        if User.query.filter_by(username=form.username.data).first():
            flash('User {} is already registered.'.format(form.username.data))
        user=User(username=form.username.data,password=form.password.data,email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)




