from flask_uploads import UploadSet,IMAGES
from flask_bcrypt import Bcrypt

bcrypt= Bcrypt()

file=UploadSet('files')
images=UploadSet('image',IMAGES)