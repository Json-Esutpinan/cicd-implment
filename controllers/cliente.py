from flask import Blueprint, request, jsonify
from model import Db, Cliente

cliente_api = Blueprint('cliente_api', __name__)
db = Db().db

@cliente_api.route('/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    cliente = Cliente(**data)
    db.session.add(cliente)
    db.session.commit()
    return jsonify({"mensaje": "Cliente creado"}), 201

@cliente_api.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify([{"id": c.id, "nombre": c.nombre, "email": c.email} for c in clientes])

@cliente_api.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    data = request.get_json()
    cliente = Cliente.query.get_or_404(id)
    cliente.nombre = data.get('nombre', cliente.nombre)
    cliente.email = data.get('email', cliente.email)
    db.session.commit()
    return jsonify({"mensaje": "Cliente actualizado"})

@cliente_api.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({"mensaje": "Cliente eliminado"})