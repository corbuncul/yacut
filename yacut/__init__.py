from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import config

app = Flask(__name__)
app.config.from_object(config)
app.json.ensure_ascii = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from yacut import api_views, error_handlers, views
