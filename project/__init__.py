import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from project.api.water_box.views import water_box_blueprint
from project.api.energy_log.views import energy_log_blueprint

app.register_blueprint(water_box_blueprint)
app.register_blueprint(energy_log_blueprint)