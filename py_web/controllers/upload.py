import os
from flask import (flash, request, redirect, url_for, Blueprint, current_app,render_template,
                   send_from_directory
                   )
from werkzeug.utils import secure_filename
from py_web.models import UploadFile
from datetime import datetime
from py_web.database import db
upload = Blueprint('upload', __name__, url_prefix='/upload')

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','xlsx','csv'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@upload.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)
            new_file=UploadFile(filename)
            new_file.upload_date=datetime.now()
            db.session.add(new_file)
            db.session.commit()
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload.file_list'))
    return render_template('upload/upload.html')
@upload.route('/file_list',methods=['GET'])
def file_list():
    file=UploadFile.query.all()
    return render_template('upload/file_list.html',file=file)


@upload.route('/download/<int:id>')
def uploaded_file(id):
    file=UploadFile.query.get(id)
    return send_from_directory(current_app.config['UPLOAD_FOLDER'],
                                   file.filename)