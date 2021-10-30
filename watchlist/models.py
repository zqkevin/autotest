# -*- coding: utf-8 -*-
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from watchlist import db
import time

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))
    filename = db.Column(db.String(80))

class Ethusdt1m(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    opentime = db.Column(db.DateTime)
    openpr = db.Column(db.Float)
    hightpr = db.Column(db.Float)
    lowpr = db.Column(db.Float)
    closepr = db.Column(db.Float)
    bustur = db.Column(db.Float)
    closetime = db.Column(db.DateTime)
    busvolu = db.Column(db.Float)
    busnum = db.Column(db.Integer)
    actbustur = db.Column(db.Float)
    actbusvolu = db.Column(db.Float)

    def stamptodatetime(self):
        self.opentime = datetime.fromtimestamp(int(self.opentime/1000))
        self.closetime = datetime.fromtimestamp(int(self.closetime/1000))
    def datetimetostamp(self):
        self.opentime = int(self.opentime.timestamp())*1000
        self.closetime = int(self.closetime.timestamp())*1000


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ordertime = db.Column(db.DateTime)
    time = db.Column(db.DateTime)
    orderid = db.Column(db.INT)
    side = db.Column(db.String(30))
    price = db.Column(db.Float)
    origqty = db.Column(db.Float)
    status = db.Column(db.String(30))


