
CREATE_TABLE_PRODUCT_SQL = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        description VARCHAR(255) NOT NULL,
        stock INTEGER NOT NULL DEFAULT 0,
        price DECIMAL(10, 3) NOT NULL
    );
"""

CREATE_PRODUCT_SQL = "INSERT INTO products (name, description, stock, price) VALUES (?, ?, ?, ?)"

GET_PRODUCT_SQL = "SELECT * FROM products"

GET_PRODUCT_BY_ID_SQL = "SELECT * FROM products WHERE id = ?"

DELETE_PRODUCT_BY_ID_SQL = "DELETE FROM products WHERE id = ?"

GET_PRODUCT_COUNT_SQL = "SELECT COUNT(*) FROM products"

UPDATE_PRODUCT_SQL = "UPDATE products SET name = ?, description = ?, stock = ?, price = ? WHERE id = ?"