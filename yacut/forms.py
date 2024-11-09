from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    """Форма ввода укорачивателя ссылок.

    поля:
        original_link (URLField):   обязательное поле для ввода ссылки
                                    на оригинальную страницу.
        custom_id (StringField):    опциональное поле для ввода желаемой
                                    пользователем короткой ссылки.
        submit (SubmitField):       кнопка "Создать"
    """
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'), Length(1, 256)],
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки', validators=[Length(1, 16), Optional()]
    )
    submit = SubmitField('Создать')
