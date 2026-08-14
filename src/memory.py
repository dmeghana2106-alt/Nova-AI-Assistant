import sqlite3


class Memory:

    def __init__(self):
        self.connection = sqlite3.connect("data/nova_memory.db")
        self.create_table()

    def create_table(self):
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                information TEXT
            )
        """)
        self.connection.commit()

    def save(self, information):
        self.connection.execute(
            "INSERT INTO memories (information) VALUES (?)",
            (information,)
        )
        self.connection.commit()

    def get_all(self):
        cursor = self.connection.execute(
            "SELECT information FROM memories"
        )

        return [row[0] for row in cursor.fetchall()]