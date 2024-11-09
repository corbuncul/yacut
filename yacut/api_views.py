from http import HTTPStatus
import re

from flask import jsonify, request, url_for

from yacut import app, db
from yacut.constants import (
    INVALID_NAME,
    NOT_FOUND,
    REQUIRED_FIELD,
    REQUEST_BODY_IS_MISSING,
    SHORT_LINK_EXIST,
    SHORT_LINK_CHECK,
)
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def shortener():
    """Представление API для создания короткой ссылки."""
    data = request.get_json(force=True, silent=True)
    if data is None:
        raise InvalidAPIUsage(REQUEST_BODY_IS_MISSING)
    if 'url' not in data:
        raise InvalidAPIUsage(REQUIRED_FIELD)
    if 'custom_id' in data:  # пустую строку тоже обработать
        short_id = data['custom_id']

        if short_id == '':
            short_id = get_unique_short_id()

        if re.match(SHORT_LINK_CHECK, short_id) is None:
            raise InvalidAPIUsage(INVALID_NAME)

        if URLMap.query.filter_by(short=short_id).first() is not None:
            raise InvalidAPIUsage(SHORT_LINK_EXIST)

        short = short_id
    else:
        short = get_unique_short_id()
    original = data['url']
    urlmap = URLMap(original=original, short=short)
    db.session.add(urlmap)
    db.session.commit()
    short_link = url_for('to_original_view', short_id=short, _external=True)
    return (
        jsonify({'url': original, 'short_link': short_link}),
        HTTPStatus.CREATED,
    )


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_url(short_id):
    """Представление API для получения адреса оригинальной страницы."""
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is None:
        raise InvalidAPIUsage(NOT_FOUND, HTTPStatus.NOT_FOUND)
    return jsonify({'url': urlmap.original}), HTTPStatus.OK
