from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class Producto(db.Model):
    id = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String)
    precio = db.Column(db.Float, nullable=False)