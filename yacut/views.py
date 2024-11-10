import re
from flask import flash, redirect, render_template, url_for
from http import HTTPStatus

from yacut import app, db
from yacut.constants import SHORT_LINK_EXIST, SHORT_LINK_CHECK, INVALID_NAME
from yacut.forms import URLMapForm
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def shortener_view():
    """Представление для главной страницы укорачивателя ссылок."""
    form = URLMapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if custom_id:
            if re.match(SHORT_LINK_CHECK, custom_id) is None:
                flash(INVALID_NAME)
                return render_template('shortener.html', form=form)
            if URLMap.query.filter_by(short=custom_id).first() is not None:
                flash(SHORT_LINK_EXIST)
                return render_template('shortener.html', form=form)
            short = custom_id
        else:
            short = get_unique_short_id()
        urlmap = URLMap(original=form.original_link.data, short=short)
        short_link = url_for(
            'to_original_view', short_id=short, _external=True
        )
        message = f'<a href="{short_link}">{short_link}</a>'
        flash(message)
        db.session.add(urlmap)
        db.session.commit()
        return render_template('shortener.html', form=form)
    return render_template('shortener.html', form=form)


@app.route('/<string:short_id>')
def to_original_view(short_id):
    """Перенаправление на оригинальную станицу."""
    urlmap = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(urlmap.original, code=HTTPStatus.FOUND)
