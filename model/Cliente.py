from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Cliente(db.Model):
    id = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    apellido = db.Column(db.String, nullable=False)