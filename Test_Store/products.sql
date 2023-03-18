CREATE TABLE products (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  price DECIMAL(10, 2),
  image_url VARCHAR(255)
);

INSERT INTO products (id, name, price, image_url)
VALUES
  (1, 'Product 1', 10.00, 'https://example.com/images/product1.jpg'),
  (2, 'Product 2', 20.00, 'https://example.com/images/product2.jpg'),
  (3, 'Product 3', 30.00, 'https://example.com/images/product3.jpg'),
  (4, 'Product 4', 40.00, 'https://example.com/images/product4.jpg'),
  (5, 'Product 5', 50.00, 'https://example.com/images/product5.jpg');