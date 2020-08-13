from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    file = FileField('File', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Upload')
