from models import Inventory
import uuid


def populate_inventory(data):
    new_inventory = Inventory(public_id=str(uuid.uuid4()),
                              store_id=data['store_id'],
                              product_id=data['product_id'],
                              price=data['price'],
                              quantity=data['quantity']
                              )
    return new_inventory


def allocate_data(inventory):
    inventory_data = {'public_id': inventory.public_id,
                      'store_id': inventory.store_id,
                      'product_id': inventory.product_id,
                      'quantity': inventory.quantity,
                      'price': inventory.price,
                      }
    return inventory_data


def combine_results(inventories):
    output = []
    for inventory in inventories:
        inventory_data = allocate_data(inventory)
        output.append(inventory_data)
    return output
