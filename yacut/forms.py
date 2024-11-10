from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional

ORIGINAL_MAX_LENGHT = 256
ORIGINAL_MIN_LENGHT = 1
CUSTOM_MAX_LENGHT = 16
CUSTOM_MIN_LENGHT = 1


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
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(ORIGINAL_MIN_LENGHT, ORIGINAL_MAX_LENGHT)
        ],
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(CUSTOM_MIN_LENGHT, CUSTOM_MAX_LENGHT),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
