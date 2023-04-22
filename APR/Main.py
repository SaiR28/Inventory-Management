from flask import Flask, render_template, request,redirect,abort,url_for
import os
import sqlite3
from flask import jsonify
app = Flask(__name__)

# Construct the path to the database file
db_filename = 'inventory.db'
db_path = os.path.join(os.getcwd(), db_filename)

@app.route('/', methods=['GET'])
def home():
    # Connect to the database and fetch all products
    conn = sqlite3.connect(db_path)
    cursor = conn.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()

    # Render the home template with the list of products
    return render_template('home.html', products=products)


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

@app.route('/delete_product/<int:id>', methods=['POST'])
def delete_product(id):
    # Connect to the database
    conn = sqlite3.connect(db_path)

    # Delete the product with the given id from the products table
    conn.execute('DELETE FROM products WHERE id = ?', (id,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Redirect to the products list page
    return redirect('/products')

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

@app.route('/modify_product/<int:id>', methods=['GET', 'POST'])
def modify_product(id):
    # Connect to the database and get the product with the given id
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE id = ?', (id,))
    product = cursor.fetchone()
    conn.close()

    if product is None:
        # If no product was found with the given id, return a 404 error
        return abort(404)

    if request.method == 'POST':
        # Get the form data from the request
        name = request.form['name']
        category = request.form['category']
        price = request.form['price']
        quantity = request.form['quantity']

        # Connect to the database and update the product with the new data
        conn = sqlite3.connect(db_path)
        conn.execute('UPDATE products SET name = ?, category = ?, price = ?, quantity = ? WHERE id = ?',
                     (name, category, price, quantity, id))
        conn.commit()
        conn.close()

        # Redirect to the products list page
        return redirect('/products')

    # If the request is not a POST request, render the modify product form with the product's current data
    return render_template('modify_product.html', product=product)


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
    
@app.route('/api/info/<int:id>', methods=['GET'])
def api_get_product(id):
    # Connect to the database and get the product with the given id
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE id = ?', (id,))
    product = cursor.fetchone()
    conn.close()

    if product is None:
        # If no product was found with the given id, return a 404 error
        return abort(404)

    # Return a JSON response containing the product information
    return jsonify({
        'id': product[0],
        'name': product[1],
        'category': product[2],
        'price': product[3],
        'quantity': product[4]
    })

if __name__ == '__main__':
    app.run(debug=True)