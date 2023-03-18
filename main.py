import sqlite3

def create_table():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products
                    (id INTEGER PRIMARY KEY,
                     name TEXT,
                     quantity INTEGER,
                     price REAL)''')
    conn.commit()
    conn.close()

def add_product():
    name = input('Enter the product name: ')
    quantity = int(input('Enter the product quantity: '))
    price = float(input('Enter the product price: '))
    
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO products (name, quantity, price)
                      VALUES (?, ?, ?)''', (name, quantity, price))
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

create_table()

while True:
    print('\n1. Add product')
    print('2. View products')
    print('3. Exit')
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
        break
    else:
        print('Invalid choice.')