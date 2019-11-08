from flask import Blueprint, request, jsonify
from project.api.water_box.model import WaterBox

from sqlalchemy import exc
from project import db

water_box_blueprint = Blueprint('/water-box', __name__)

@water_box_blueprint.route('/water_box', methods=['POST'])
def create_water_box():
    data = request.get_json()

    if not data:
        return jsonify({
            'error': 'Water box can not be created'
        }), 400

    material        = data.get('material')
    volume          = data.get('volume')
    position        = data.get('position')
    pipe_size       = data.get('pipe_size')

    try:
        water_box = WaterBox(material, volume, position, pipe_size)
        db.session.add(water_box)
        db.session.commit()

        return jsonify({
            'status': 'success',
            'data': {
                'message': 'Water box was created'
            }
        }), 200
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({
            'error': 'Water box can not be created'
        }), 400

@water_box_blueprint.route('/water_box/<int:id>', methods=['GET'])
def get_water_box(id):
    water_box = WaterBox.query.filter_by(id=id).first()

    return jsonify({
        'water_box': water_box.to_json()
    })