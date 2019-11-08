from sqlalchemy.sql import func
from project import db

class EnergyLog(db.Model):
    __tablename__ = 'energy_log'
    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    current         = db.Column(db.Float, nullable=True)
    power           = db.Column(db.Float, nullable=True)
    time            = db.Column(db.DateTime, nullable=False)
    is_working      = db.Column(db.Boolean, nullable=False)
    water_box_id    = db.Column(db.Integer, db.ForeignKey('water_box.id') , nullable=False)

    def __init__(self, current, power, time, is_working, water_box_id):
        self.current        = current
        self.power          = power
        self.time           = time
        self.is_working     = is_working
        self.water_box_id   = water_box_id

    def to_json(self):
        return {
            'id': self.id,
            'current': self.current,
            'power': self.power,
            'time': self.time,
            'is_working': self.is_working,
            'water_box_id': self.water_box_id
        }