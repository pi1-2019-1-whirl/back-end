from sqlalchemy.sql import func
from project import db

class WaterBox(db.Model):
    __tablename__ = 'water_box'
    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_working      = db.Column(db.Boolean, nullable=True)

    def __init__(self, is_working):
        self.is_working = is_working

    def to_json(self):
        return {
            'id': self.id,
            'is_working': self.is_working
        }