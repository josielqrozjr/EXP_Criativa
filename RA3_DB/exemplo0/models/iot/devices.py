from models.db import db

class Device(db.Model):
    __tablename__ = 'devices'
    id= db.Column('id', db.Integer, primary_key=True)
    name= db.Column(db.String(100))
    brand= db.Column(db.String(100))
    model= db.Column(db.String(50))
    is_active= db.Column(db.Boolean, nullable= False, default= False)
    sensors = db.relationship('Sensor', backref='devices', lazy=True)
    actuator = db.relationship('Actuator', backref='devices', lazy=True)
