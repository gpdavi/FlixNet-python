import os
import sqlite3

class CustomerArchive:
    def __init__(self):
        self.__customers = []

    def add(self, customer):
        self.__customers.append(customer)

    def getCustomers(self):
        return self.__customers

    @staticmethod
    def connection(way_db: str = None) -> sqlite3.Connection:
        if way_db is None:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            PARENT_DIR = os.path.dirname(BASE_DIR)
            DB_DIR = os.path.join(PARENT_DIR, "data")
            os.makedirs(DB_DIR, exist_ok=True)
            way_db = os.path.join(DB_DIR, "manager.db")

        conn = sqlite3.connect(way_db)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    @staticmethod
    def table(conn: sqlite3.Connection) -> None:
        """Cria as tabelas do banco (se ainda não existirem)."""
        with conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS manager (
                    id      INTEGER PRIMARY KEY AUTOINCREMENT,
                    name    TEXT    NOT NULL,
                    username    TEXT   NOT NULL,
                    password    TEXT    NOT NULL,
                    address     TEXT    NOT NULL
                )""")

    @staticmethod
    def insert_customer(conn: sqlite3.Connection, name: str, username: str, password: str, address: str) -> None:
        with conn:
            conn.execute("""
                INSERT INTO manager (name, username, password, address)
                VALUES (?, ?, ?, ?)
            """, (name, username, password, address))