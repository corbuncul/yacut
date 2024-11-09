from http import HTTPStatus

from flask import jsonify, render_template

from yacut import app, db


class InvalidAPIUsage(Exception):
    """Исключение при ошибках использования API."""
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        """Возвращает сообщение об ошибке в виде словаря."""
        return {'message': self.message}


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    """Обработчик исключения InvalidAPIUsage.

    Возвращает кортеж состоящий из объекта JSON с сообщением об ошибке
    и кода ошибки.
    """
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error):
    """Обработчик ошибки 404 - не найдено."""
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error):
    """Обработчик ошибки 500 - внутренней ошибки сервера."""
    db.session.rollback()
    return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR
