import os
from flask import (flash, request, redirect, url_for, Blueprint, current_app,render_template,
                   send_from_directory
                   )
from werkzeug.utils import secure_filename
from py_web.models import UploadFile
from datetime import datetime
from py_web.database import db
from py_web.ext import file
from py_web.forms import UploadForm,LoginForm




upload = Blueprint('upload', __name__, url_prefix='/upload')

#
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@upload.route('/', methods=['GET', 'POST'])
def upload_file():
    form=UploadForm()
    if form.validate_on_submit():
        filename = file.save(request.files['files'])
        if filename:
            filename = secure_filename(file.filename)
            new_file=UploadFile(filename)
            new_file.upload_date=datetime.now()
            db.session.add(new_file)
            db.session.commit()
            flash('file uploaded',category='success')
            return redirect(url_for('upload.file_list'))
    return render_template('upload/upload.html',form=form)

@upload.route('/file_list',methods=['GET'])
def file_list():
    file=UploadFile.query.all()
    return render_template('upload/file_list.html',file=file)


@upload.route('/download/<int:id>')
def uploaded_file(id):
    file=UploadFile.query.get(id)
    return send_from_directory(current_app.config['UPLOAD_FOLDER'],
                                   file.filename)


@upload.route('/1')
def test_forms():
    form=LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('upload/test_form.html',form=form)