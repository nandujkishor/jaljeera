from flask import Flask, Blueprint
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('openapi.yaml')
app.app.config.from_object(Config)
db = SQLAlchemy(app.app)
migrate = Migrate(app.app, db)
fapp = app.app

from app import routes, models, events, collections
