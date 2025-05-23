from flask import Blueprint, request, jsonify
from model import Cliente, Producto, Pedido
from model.Db import db

api = Blueprint('api', __name__)
@api.route('/productos/<int:id>', methods=['PUT'])
def update_producto(id):
    data = request.get_json()
    producto = Producto.query.get_or_404(id)
    producto.nombre = data.get('nombre', producto.nombre)
    producto.descripcion = data.get('descripcion', producto.descripcion)
    producto.precio = data.get('precio', producto.precio)
    db.session.commit()
    return jsonify({"mensaje": "Producto actualizado"})

@api.route('/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({"mensaje": "Producto eliminado"})

@api.route('/productos', methods=['POST'])
def create_producto():
    data = request.get_json()
    producto = Producto(**data)
    db.session.add(producto)
    db.session.commit()
    return jsonify({"mensaje": "Producto creado"}), 201

@api.route('/productos', methods=['GET'])
def get_productos():
    return jsonify([{"id": p.id, "nombre": p.nombre, "descripcion": p.descripcion, "precio": p.precio} for p in Producto.query.all()])