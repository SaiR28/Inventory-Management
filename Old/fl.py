from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Define the API endpoint to decrease the quantity of a product by name in the URL
@app.route('/decrease_quantity/<name>/<int:quantity>', methods=['GET'])
def decrease_quantity(name, quantity):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Check if the product with the given name exists
    cursor.execute('SELECT * FROM products WHERE name = ?', (name,))
    product = cursor.fetchone()
    if product is None:
        return jsonify({'error': f'Product with name {name} does not exist.'}), 404

    # Check if the quantity to be decreased is greater than the current quantity of the product
    if quantity > product[2]:
        return jsonify({'error': f'Quantity to be decreased ({quantity}) is greater than the current quantity ({product[2]}) of the product.'}), 400

    # Decrease the quantity of the product
    cursor.execute('UPDATE products SET quantity = quantity - ? WHERE name = ?', (quantity, name))
    conn.commit()
    conn.close()

    return jsonify({'message': f'Quantity of product {name} decreased by {quantity}.'}), 200

if __name__ == '__main__':
    app.run(debug=True)