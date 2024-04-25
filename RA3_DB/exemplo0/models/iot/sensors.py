from models.db import db
from models.iot.devices import Device

class Sensor(db.Model):
    __tablename__ = 'sensors'
    id= db.Column('id', db.Integer, primary_key=True)
    devices_id = db.Column( db.Integer, db.ForeignKey(Device.id))
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))


    def save_sensor(name, brand, model, topic, unit, is_active):
        device = Device(name = name, 
                        brand = brand, 
                        model = model, 
                        is_active = is_active)
        sensor = Sensor(devices_id = device.id, 
                        unit= unit, 
                        topic = topic)
        
        device.sensors.append(sensor)
        db.session.add(device)
        db.session.commit()
