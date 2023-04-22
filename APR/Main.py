from flask import Flask, render_template, request,redirect
import os
import sqlite3
from flask import jsonify
app = Flask(__name__)

# Construct the path to the database file
db_filename = 'inventory.db'
db_path = os.path.join(os.getcwd(), db_filename)



# If the database file doesn't exist, create it and the products table
if not os.path.exists(db_path):
    # Connect to the database
    conn = sqlite3.connect(db_path)

    # Create the products table
    conn.execute('''
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price REAL,
            quantity INTEGER
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Define a route for adding products
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Get the form data from the request
        name = request.form['name']
        category = request.form['category']
        price = request.form['price']
        quantity = request.form['quantity']

        print(name, category, price, quantity)  # Debugging line

        # Connect to the database
        conn = sqlite3.connect(db_path)

        # Insert the product into the products table
        conn.execute('INSERT INTO products (name, category, price, quantity) VALUES (?, ?, ?, ?)',
                     (name, category, price, quantity))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Redirect to the products list page
        return redirect('/products')

    # If the request is not a POST request, render the add product form
    return render_template('add_product.html')

# Define a route for deleting a product
@app.route('/products')
def products():
    # Connect to the database and fetch all products
    conn = sqlite3.connect(db_path)
    cursor = conn.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()

    # Render the products list template with the list of products
    return render_template('products.html', products=products)

@app.route('/api/sale/<int:id>/<int:quantity>', methods=['PUT'])
def api_sale(id, quantity):
    # Connect to the database and update the quantity of the product with the given id
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT quantity FROM products WHERE id = ?', (id,))
    current_quantity = cursor.fetchone()[0]
    new_quantity = current_quantity - quantity
    conn.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, id))
    conn.commit()
    conn.close()

    # Return a JSON response indicating the new quantity of the product
    return jsonify({'id': id, 'quantity': new_quantity})
    

if __name__ == '__main__':
    app.run(debug=True)