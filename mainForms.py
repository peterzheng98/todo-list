from flask_wtf import FlaskForm
from wtforms.validators import ValidationError, DataRequired
from wtforms import StringField, SubmitField, TextAreaField


class addWorkForm(FlaskForm):
    title = StringField(validators=[DataRequired()], render_kw={
            'class': 'form-control monospace',
            'placeholder': '标题'
    })
    context = TextAreaField(render_kw={
        'class': 'form-control monospace',
        'placeholder': '内容描述'
    })
    submit = SubmitField(
        '提交', render_kw={
            'class': "btn btn-primary",
            'id': "submit_login"
        }
    )