import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    from project.api.water_box.views import water_box_blueprint
    app.register_blueprint(water_box_blueprint)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}
    return app