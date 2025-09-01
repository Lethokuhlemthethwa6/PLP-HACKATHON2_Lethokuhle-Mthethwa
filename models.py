from flask_mysqldb import MySQL # pyright: ignore[reportMissingImports]

mysql = MySQL()

def init_db(app):
    mysql.init_app(app)

def create_tables():
    cursor = mysql.connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            mood VARCHAR(50),
            reflection TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    mysql.connection.commit()
    cursor.close()
