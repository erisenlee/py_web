from flask_uploads import UploadSet,IMAGES,DEFAULTS
from flask_bcrypt import Bcrypt

bcrypt= Bcrypt()

file=UploadSet('files',DEFAULTS)
images=UploadSet('image',IMAGES)