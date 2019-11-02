import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)


app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from project.api.water_box.views import water_box_blueprint
app.register_blueprint(water_box_blueprint)