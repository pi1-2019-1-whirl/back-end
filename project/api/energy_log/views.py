from flask import Blueprint, request, jsonify
from project.api.energy_log.model import EnergyLog
from project.api.water_box.model import WaterBox
from datetime import datetime

from sqlalchemy import exc
from project import db

energy_log_blueprint = Blueprint('/energy-log', __name__)

@energy_log_blueprint.route('/energy_log/<int:id>', methods=['POST'])
def create_energy_log(id):
    data = request.get_json()

    if not data:
        return jsonify({
            'status': 'Fail',
            'message': 'Energy log can not be created'
        }), 400

    water_box = WaterBox.query.filter_by(id=id).first()

    if not water_box:
        return jsonify({
            'status': 'Fail',
            'message': 'Water box does not exist'
        }), 404

    current         = data.get('current')
    power           = data.get('power')
    time            = datetime.now()
    is_working      = data.get('is_working')
    water_box_id    = id

    try:
        energy_log = EnergyLog(current, power, time, is_working, water_box_id)
        db.session.add(energy_log)
        db.session.commit()

        return jsonify({
            'status': 'Success',
            'message': 'Energy log was created'
        }), 200
    except exc.IntegrityError:
        db.session.rollbac()
        return jsonify({
            'status': 'Fail',
            'message': 'Energy log can not be created'
        }), 400