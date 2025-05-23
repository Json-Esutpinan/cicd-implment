from flask import Blueprint, request, jsonify
from model import Db, Pedido, Producto

pedido_api = Blueprint('pedido_api', __name__)
db = Db().db

@pedido_api.route('/pedidos', methods=['POST'])
def create_pedido():
    data = request.get_json()
    producto_ids = data.pop('producto_ids', [])
    pedido = Pedido(**data)
    if producto_ids:
        productos = Producto.query.filter(Producto.id.in_(producto_ids)).all()
        pedido.productos = productos
        # Calcular el total sumando los precios de los productos
        pedido.total = sum(p.precio for p in productos)
    else:
        pedido.total = 0.0
    db.session.add(pedido)
    db.session.commit()
    return jsonify({"mensaje": "Pedido creado"}), 201

@pedido_api.route('/pedidos', methods=['GET'])
def get_pedidos():
    pedidos = Pedido.query.all()
    return jsonify([
        {
            "id": p.id,
            "cliente_id": p.cliente_id,
            "total": p.total,
            "productos": [{"id": prod.id, "nombre": prod.nombre} for prod in p.productos]
        }
        for p in pedidos
    ])

@pedido_api.route('/pedidos/<int:id>', methods=['PUT'])
def update_pedido(id):
    data = request.get_json()
    producto_ids = data.pop('producto_ids', None)
    pedido = Pedido.query.get_or_404(id)
    pedido.cliente_id = data.get('cliente_id', pedido.cliente_id)
    if producto_ids is not None:
        productos = Producto.query.filter(Producto.id.in_(producto_ids)).all()
        pedido.productos = productos
        pedido.total = sum(p.precio for p in productos)
    db.session.commit()
    return jsonify({"mensaje": "Pedido actualizado"})

@pedido_api.route('/pedidos/<int:id>', methods=['DELETE'])
def delete_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return jsonify({"mensaje": "Pedido eliminado"})