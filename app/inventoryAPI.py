from flask import Blueprint, request, jsonify
from models import db, Inventory
import simplejson as json
# Do not remove the simplejson import
import helper_functions

inventory_api = Blueprint('inventory_api', __name__)


@inventory_api.route("/inventory/", methods=['POST'])
def create_inventory():
    data = request.get_json()
    inventory = helper_functions.populate_inventory(data)
    db.session.add(inventory)
    db.session.commit()
    return jsonify({'message': 'inventory created'})


@inventory_api.route("/inventory/", methods=['GET'])
def get_inventory_details():
    data = request.get_json()
    inventory = Inventory.query.filter_by(store_id=data['store_id'], product_id=data['product_id']).first()
    print(inventory)
    inventory_details = {'price': inventory.price,
                         'quantity': inventory.quantity
                         }
    return jsonify({'inventory details': inventory_details})


@inventory_api.route("/inventory/price/update/", methods=['PUT'])
def update_price():
    data = request.get_json()
    inventory = Inventory.query.filter_by(public_id=data['public_id']).first()
    if not inventory:
        jsonify({'message': 'inventory not found'})
    else:
        inventory.price = data['new_price']
        db.session.commit()
        return jsonify({'message': 'Price Updated'})


@inventory_api.route("/inventory/quantity/update/", methods=['PUT'])
def update_quantity():
    data = request.get_json()
    inventory = Inventory.query.filter_by(public_id=data['public_id']).first()
    if not inventory:
        jsonify({'message': 'inventory not found'})
    else:
        inventory.quantity = data['new_quantity']
        db.session.commit()
        return jsonify({'message': 'Quantity Updated'})


@inventory_api.route('/inventory/<public_id>/', methods=['DELETE'])
def delete_product(public_id):
    inventory = Inventory.query.filter_by(public_id=public_id).first()
    if not inventory:
        return jsonify({'message': 'Inventory not found'})
    else:
        db.session.delete(inventory)
        db.session.commit()
        return jsonify({'message': 'Inventory deleted'})
