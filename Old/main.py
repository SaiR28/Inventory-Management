import sqlite3

def create_table():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products
                    (id INTEGER PRIMARY KEY,
                     name TEXT,
                     sku TEXT,
                     supplier TEXT,
                     quantity INTEGER,
                     price REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS suppliers
                    (id INTEGER PRIMARY KEY,
                     name TEXT,
                     email TEXT,
                     sku TEXT)''')
    conn.commit()
    conn.close()

def add_product():
    name = input('Enter the product name: ')
    sku = input('Enter the product SKU: ')
    supplier = input('Enter the supplier name: ')
    quantity = int(input('Enter the product quantity: '))
    price = float(input('Enter the product price: '))
    
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO products (name, sku, supplier, quantity, price)
                      VALUES (?, ?, ?, ?, ?)''', (name, sku, supplier, quantity, price))
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

def add_supplier():
    name = input('Enter the supplier name: ')
    email = input('Enter the supplier email: ')
    sku = input('Enter the supplier SKU: ')
    
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO suppliers (name, email, sku)
                      VALUES (?, ?, ?)''', (name, email, sku))
    conn.commit()
    conn.close()

def get_suppliers():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM suppliers')
    suppliers = cursor.fetchall()
    conn.close()
    return suppliers

create_table()

while True:
    print('\n1. Add product')
    print('2. View products')
    print('3. Add supplier')
    print('4. View suppliers')
    print('5. Exit')
    choice = int(input('Enter your choice: '))
    
    if choice == 1:
        add_product()
        print('Product added successfully!')
    elif choice == 2:
        products = get_products()
        if len(products) > 0:
            print('\nID\tName\tQuantity\tPrice')
            for product in products:
                print(f'{product[0]}\t{product[1]}\t{product[2]}\t{product[3]}')
        else:
            print('No products found.')
    elif choice == 3:
        add_supplier()
        print('Supplier added successfully!')
    elif choice == 4:
        suppliers = get_suppliers()
        if len(suppliers) > 0:
            print('\nID\tName\tEmail\tSKU')
            for supplier in suppliers:
                print(f'{supplier[0]}\t{supplier[1]}\t{supplier[2]}\t{supplier[3]}')
        else:
            print('No suppliers found.')
    elif choice == 5:
        break
    else:
        print('Invalid choice.')
