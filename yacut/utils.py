import random
import string

from yacut.constants import LENGHT_SHOT_LINK
from yacut.models import URLMap


def get_unique_short_id(lenght=LENGHT_SHOT_LINK):
    """Генератор уникальных коротких ссылок."""
    while True:
        short_link = ''.join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(lenght)
        )
        if URLMap.query.filter_by(short=short_link).first() is None:
            break
    return short_link
