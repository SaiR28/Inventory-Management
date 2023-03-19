import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def add_product():
    name = name_entry.get()
    quantity = int(quantity_entry.get())
    price = float(price_entry.get())
    
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO products (name, quantity, price)
                      VALUES (?, ?, ?)''', (name, quantity, price))
    conn.commit()
    conn.close()
    
    messagebox.showinfo('Success', 'Product added successfully!')
    clear_entries()

def get_products():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

def view_products():
    products = get_products()
    if len(products) > 0:
        for i in products_treeview.get_children():
            products_treeview.delete(i)
        for product in products:
            products_treeview.insert('', 'end', text=product[0], values=(product[1], product[2], product[3]))
    else:
        messagebox.showinfo('Error', 'No products found.')
    
def clear_entries():
    name_entry.delete(0, 'end')
    quantity_entry.delete(0, 'end')
    price_entry.delete(0, 'end')
    
root = tk.Tk()
root.title('Inventory Management System')

# Set the window size and position
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Create the product entry labels and fields
name_label = tk.Label(root, text='Product Name')
name_entry = tk.Entry(root)

quantity_label = tk.Label(root, text='Product Quantity')
quantity_entry = tk.Entry(root)

price_label = tk.Label(root, text='Product Price')
price_entry = tk.Entry(root)

name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry.grid(row=0, column=1, padx=5, pady=5)

quantity_label.grid(row=1, column=0, padx=5, pady=5)
quantity_entry.grid(row=1, column=1, padx=5, pady=5)

price_label.grid(row=2, column=0, padx=5, pady=5)
price_entry.grid(row=2, column=1, padx=5, pady=5)

# Create the product entry button
add_product_button = tk.Button(root, text='Add Product', command=add_product, width=30)
add_product_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create the product view table
products_treeview = ttk.Treeview(root, columns=('Name', 'Quantity', 'Price'), show='headings')
products_treeview.heading('Name', text='Name')
products_treeview.heading('Quantity', text='Quantity')
products_treeview.heading('Price', text='Price')
products_treeview.column('Name', width=120)
products_treeview.column('Quantity', width=80)
products_treeview.column('Price', width=80)
products_treeview.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create the product view button
view_products_button = tk.Button(root, text='View Products', command=view_products)
view_products_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

style = ttk.Style()
style.configure('Treeview', rowheight=30)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.rowconfigure(4, weight=1)


root.geometry('400x500')
root.configure(padx=10, pady=10)

root.mainloop()