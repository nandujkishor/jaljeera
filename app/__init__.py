from flask import Flask, Blueprint
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('openapi.yaml')
fapp = app.app
fapp.config.from_object(Config)
db = SQLAlchemy(fapp)
migrate = Migrate(app, db)

from app import routes, models, events, collections
