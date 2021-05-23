from app import db
from datetime import datetime


class Location(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(60), unique=True, nullable=False)
    place = db.relationship('Asset', backref='location')
    
    def __repr__(self):
        return f"Location('{self.location}')"


class Asset_Type (db.Model):
    __tablename__ = 'asset_type'

    id = db.Column(db.Integer, primary_key=True)
    asset_type = db.Column(db.String(60), unique=False, nullable=False)
    types = db.relationship('Asset', backref='asset_type')

    def __repr__(self):
        return f"Asset_Type('{self.asset_type}')"


class Asset(db.Model):
    __tablename__ = 'asset'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=False, nullable=False)
    asset_type_id = db.Column(db.Integer, db.ForeignKey('asset_type.id'), unique=False, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), unique=False, nullable=False)
    asset_delay = db.relationship('Delayance', backref='asset')
    def __repr__(self):
        return f"Asset('{self.name}')"


class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(60), unique=False, nullable=False)
    dept = db.relationship('Delayance', backref='department')
    
    def __repr__(self):
        return f"Department('{self.department}')"



class Delayance (db.Model):
    __tablename__ = 'delayance'

    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), unique=False, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), unique=False, nullable=False)
    time_from = db.Column(db.Time, nullable=False) 
    time_to = db.Column(db.Time, nullable=False)
    date = db.Column(db.Date, nullable = False)
    action = db.Column(db.String(200), unique=False, nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Delayance('{self.time_from}', '{self.time_to}', '{self.date}', '{self.action}')"

