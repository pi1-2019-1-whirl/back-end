from sqlalchemy.sql import func
from project import db

class WaterBox(db.Model):
    __tablename__ = 'water_box'
    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    current         = db.Column(db.Float, nullable=True)
    power           = db.Column(db.Float, nullable=True)
    time            = db.Column(db.DateTime, nullable=True)
    turbine_id      = db.Column(db.Integer, nullable=False)

    def __init__(self, current, power, time, turbine_id):
        self.current        = current
        self.power          = power
        self.time           = time
        self.turbine_id     = turbine_id

    def to_json(self):
        return {
            'id': self.id,
            'current': self.current,
            'power': self.power,
            'time': self.time,
            'turbine_id': self.turbine_id
        }