from flask import Blueprint, request, jsonify
from models import db, Inventory
import helper_functions

inventory_api = Blueprint('inventory_api', __name__)


@inventory_api.route("/inventory/", methods=['POST'])
def create_inventory():
    data = request.get_json()
    inventory = helper_functions.populate_inventory(data)
    db.session.add(inventory)
    db.session.commit()
    return jsonify({'message': 'inventory created'})
