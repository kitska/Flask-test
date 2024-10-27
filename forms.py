from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class YearForm(FlaskForm):
    year = IntegerField('Введіть рік', validators=[
        DataRequired(message="Це поле обов'язкове"),
        NumberRange(min=1, message="Рік повинен бути додатним цілим числом")
    ])
    submit = SubmitField('Перевірити')
