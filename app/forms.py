import flask 
from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, email_validator
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    #filename = StringField(label = "filename", description='Name of the file to be uploaded.', render_kw={'placeholder':'File name'})
    image = FileField(label = 'file', description='File to be uploaded, image files only [\'*.jpg\', \'*.png\', \'*.jpeg\', \'*.webp\']', validators = [DataRequired(), FileRequired()])
    submit = SubmitField('Upload File!')

