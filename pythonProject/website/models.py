from . import db
from flask_login import UserMixin

class Barber33(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    barber = db.Column(db.String(100))
    # date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('barber11.id'))


class Barber22(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    haircut = db.Column(db.String(100))
    # date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('barber11.id'))
    # barbers = db.relationship('Barber')


class Barber44(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.String(100))
    # date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('barber11.id'))


class Barber55(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(100))
    # date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('barber11.id'))


class Barber11(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    barbers = db.relationship('Barber33')
    haircuts = db.relationship('Barber22')
    times = db.relationship('Barber44')
    statuss = db.relationship('Barber55')
    # barbers = db.relationship('Barber')
