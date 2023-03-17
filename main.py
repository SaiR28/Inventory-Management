# Define inventory data structure
inventory = {
    'item1': {'name': 'Product A', 'price': 10.00, 'quantity': 100},
    'item2': {'name': 'Product B', 'price': 15.00, 'quantity': 50},
    'item3': {'name': 'Product C', 'price': 20.00, 'quantity': 200},
    'item4': {'name': 'Product D', 'price': 25.00, 'quantity': 75},
    'item5': {'name': 'Product E', 'price': 30.00, 'quantity': 150}
}

# Define function to update inventory levels
def update_inventory(item_id, quantity):
    if item_id in inventory:
        inventory[item_id]['quantity'] += quantity
        print(f"{quantity} units of {inventory[item_id]['name']} have been added to inventory.")
    else:
        print(f"Error: Item ID '{item_id}' not found in inventory.")

# Define function to process an order
def process_order(order):
    for item in order:
        item_id = item['item_id']
        quantity = item['quantity']
        if item_id in inventory and inventory[item_id]['quantity'] >= quantity:
            inventory[item_id]['quantity'] -= quantity
            print(f"{quantity} units of {inventory[item_id]['name']} have been sold.")
        else:
            print(f"Error: Not enough stock of '{inventory[item_id]['name']}' to fulfill order.")
            return False
    return True

# Define function to check inventory levels
def check_inventory():
    print("Current Inventory Levels:")
    for item_id, item_data in inventory.items():
        print(f"Item ID: {item_id}, Name: {item_data['name']}, Price: ${item_data['price']}, Quantity: {item_data['quantity']}")

# Test the functions
check_inventory()
update_inventory('item1', 25)
check_inventory()
order1 = [{'item_id': 'item1', 'quantity': 10}, {'item_id': 'item2', 'quantity': 20}]
process_order(order1)
check_inventory()
order2 = [{'item_id': 'item3', 'quantity': 250}, {'item_id': 'item4', 'quantity': 100}]
process_order(order2)
check_inventory()