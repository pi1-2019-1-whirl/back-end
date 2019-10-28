from sqlalchemy.sql import func
from project import db

class WaterBox(db.Model):
    __tablename__ = 'water_box'
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    material      = db.Column(db.String(128), nullable=True)
    volume        = db.Column(db.Float, nullable=True)
    position      = db.Column(db.String(128), nullable=True)
    pipe_size     = db.Column(db.Float, nullable=True)
    turbine_id    = db.Column(db.Integer, nullable=True)

    def __init__(self, material, volume, position, pipe_size, turbine_id):
        self.material       = material
        self.volume         = volume
        self.position       = position
        self.pipe_size      = pipe_size
        self.turbine_id     = turbine_id

    def to_json(self):
        return {
            'id': self.id,
            'material': self.material,
            'volume': self.volume,
            'position': self.position,
            'pipe_size': self.pipe_size,
            'turbine_id': self.turbine_id
        }