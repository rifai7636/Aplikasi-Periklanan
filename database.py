import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("periklanan")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS client (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            alamat TEXT,
            telepon TEXT
        )
        """)
        self.conn.commit()

    def insert_client(self, nama, alamat, telepon):
        self.cursor.execute(
            "INSERT INTO client (nama, alamat, telepon) VALUES (?, ?, ?)",
            (nama, alamat, telepon)
        )
        self.conn.commit()

    def update_client(self, id_client, nama, alamat, telepon):
        self.cursor.execute(
            "UPDATE client SET nama=?, alamat=?, telepon=? WHERE id=?",
            (nama, alamat, telepon, id_client)
        )
        self.conn.commit()

    def delete_client(self, id_client):
        self.cursor.execute(
            "DELETE FROM client WHERE id=?",
            (id_client,)
        )
        self.conn.commit()
