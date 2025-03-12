from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(10), nullable=False)
    fecha = db.Column(db.Date, default=datetime.date.today)
    total = db.Column(db.Float, nullable=False)

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    tamaño = db.Column(db.String(10), nullable=False)
    ingredientes = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)
