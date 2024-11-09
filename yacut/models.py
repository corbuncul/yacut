from datetime import datetime

from yacut import db


class URLMap(db.Model):
    """Модель укорачивателя ссылок.

    поля модели:
        id (Integer): уникальный порядковый номер короткой ссылки.
        original (String): ссылка на оригинальную страницу.
        short (String): уникальная часть короткой ссылки.
        timestamp (DateTime): временная метка создания короткой ссылки.
    """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), index=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
