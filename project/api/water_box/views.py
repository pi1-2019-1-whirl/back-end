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
            'status': 'Fail',
            'message': 'Water box can not be created'
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
            'message': 'Water box was created'
        }), 200
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({
            'status': 'Fail',
            'message': 'Water box can not be created'
        }), 400

@water_box_blueprint.route('/water_box/<int:id>', methods=['GET'])
def get_water_box(id):
    water_box = WaterBox.query.filter_by(id=id).first()

    return jsonify({
        'status': 'Success',
        'water_box': water_box.to_json()
    })

@water_box_blueprint.route('/water_box', methods=['GET'])
def get_all_water_box():
    water_boxes = [water_box.to_json() for water_box in WaterBox.query.all()]

    return jsonify({
        'ststus': 'Success',
        'water_boxes': water_boxes
    })

@water_box_blueprint.route('/water_box/<int:id>', methods=['DELETE'])
def delete_water_box(id):
    water_box = WaterBox.query.filter_by(id=id).first()

    if not water_box:
        return jsonify({
            'status': 'Fail',
            'message': 'Water box not found'
        }), 404

    db.session.delete(water_box)
    db.session.commit()

    return jsonify({
        'status': 'Success',
        'message': 'Water box deleted'
    })

@water_box_blueprint.route('/water_box/<int:id>', methods=['PUT'])
def edit_water_box(id):
    data = request.get_json()

    water_box = WaterBox.query.filter_by(id=id).first()

    if data['material']: 
        water_box.material = data['material']
    if data['volume']:
        water_box.volume = data['volume']
    if data['position']:
        water_box.position = data['position']
    if data['pipe_size']:
        water_box.pipe_size = data['pipe_size']

    db.session.add(water_box)
    db.session.commit()

    return jsonify({
        'status': 'Success',
        'message': 'Water box was edited'
    }), 200