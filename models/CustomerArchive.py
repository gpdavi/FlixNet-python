import os
import sqlite3


class CustomerArchive:
    def __init__(self):
        self.__customers = []

    def add(self, customer):
        self.__customers.append(customer)

    def getCustomers(self):
        return self.__customers

    # ---------- Conexões ----------

    @staticmethod
    def connection(way_db: str = None) -> sqlite3.Connection:
        """Conexão com o banco de clientes (customer.db)."""
        if way_db is None:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            PARENT_DIR = os.path.dirname(BASE_DIR)
            DB_DIR = os.path.join(PARENT_DIR, "data")
            os.makedirs(DB_DIR, exist_ok=True)
            way_db = os.path.join(DB_DIR, "customer.db")
        conn = sqlite3.connect(way_db)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    @staticmethod
    def connection_rented(way_db: str = None) -> sqlite3.Connection:
        """Conexão com o banco de alugados (rented.db)."""
        if way_db is None:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            PARENT_DIR = os.path.dirname(BASE_DIR)
            DB_DIR = os.path.join(PARENT_DIR, "data")
            os.makedirs(DB_DIR, exist_ok=True)
            way_db = os.path.join(DB_DIR, "rented.db")
        conn = sqlite3.connect(way_db)
        conn.row_factory = sqlite3.Row
        return conn

    # ------------------------------

    @staticmethod
    def table(conn: sqlite3.Connection) -> None:
        with conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS customer (
                    id      INTEGER PRIMARY KEY AUTOINCREMENT,
                    name    TEXT    NOT NULL,
                    username    TEXT   NOT NULL,
                    password    TEXT    NOT NULL,
                    address     TEXT    NOT NULL
                );""")

    @staticmethod
    def table_rented(conn: sqlite3.Connection) -> None:
        with conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS rented (
                    id      INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER NOT NULL,
                    title    TEXT    NOT NULL
                );""")

    # ---------- Operações ----------

    @staticmethod
    def insert_customer(conn: sqlite3.Connection, name: str, username: str, password: str, address: str) -> None:
        with conn:
            conn.execute("""
                INSERT INTO customer (name, username, password, address)
                VALUES (?, ?, ?, ?)
            """, (name, username, password, address))

    @staticmethod
    def insert_rented(conn: sqlite3.Connection, customer_id: int, title: str) -> None:
        with conn:
            conn.execute("""
                INSERT INTO rented (customer_id, title)
                VALUES (?, ?)
            """, (customer_id, title))

    @staticmethod
    def get_id_by_username(conn: sqlite3.Connection, username: str):
        cursor = conn.execute("""
            SELECT id FROM customer WHERE username = ?
        """, (username,))
        row = cursor.fetchone()
        return row["id"] if row else None