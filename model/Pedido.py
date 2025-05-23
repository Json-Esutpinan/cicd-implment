from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

pedido_producto = db.Table('pedido_producto',
    db.Column('pedido_id', db.Integer, db.ForeignKey('pedido.id'), primary_key=True),
    db.Column('producto_id', db.Integer, db.ForeignKey('producto.id'), primary_key=True)
)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    total = db.Column(db.Float, default=0.0)
    productos = db.relationship('Producto', secondary=pedido_producto, backref='pedidos')