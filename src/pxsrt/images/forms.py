from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, RadioField
from wtforms.fields.html5 import IntegerRangeField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    file = FileField('File', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Upload')

class ToolsForm(FlaskForm):
    mode = SelectField(
            'Mode',
            validators=[DataRequired()],
            choices=[
                    ('H', 'Hue'),
                    ('S', 'Saturation'),
                    ('V', 'Value'),
                    ('R', 'Red'),
                    ('G', 'Green'),
                    ('B', 'Blue')
                    ])
    threshold = IntegerRangeField('Threshold')
    direction = RadioField(
            'Direction', validators=[DataRequired()],
            choices=[('H', 'Horizontal'),('V', 'Vertical')])
    upper = BooleanField('Upper')
    reverse = BooleanField('Reverse')
    preview = SubmitField('Preview')
    sort = SubmitField('Sort')
    refresh = SubmitField('Refresh')
