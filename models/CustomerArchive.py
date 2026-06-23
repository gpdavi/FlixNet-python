import sqlite3
class CustomerArchive:

    def __init__(self):
        self.__customers = []
    
    def add(self, customer):
        self.__customers.append(customer)

    def getCustomers(self):
        return self.__customers
    
    @staticmethod
    def connection(way_db: str = "customer.db") -> sqlite3.Connection:
        #Cria e retorna uma conexão com o banco de dados.
        conn = sqlite3.connect(way_db)
        conn.row_factory = sqlite3.Row   # resultados acessíveis por nome de coluna
        conn.execute("PRAGMA foreign_keys = ON")  # ativa chaves estrangeiras
        return conn
    
    @staticmethod
    def table(conn: sqlite3.Connection) -> None:
        """Cria as tabelas do banco (se ainda não existirem)."""
        with conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS customer (
                    id      INTEGER PRIMARY KEY AUTOINCREMENT,
                    name    TEXT    NOT NULL,
                    username    TEXT   NOT NULL,
                    password    TEXT    NOT NULL,
                    address     TEXT    NOT NULL
                );
                CREATE TABLE IF NOT EXISTS rented (
                    id      INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER NOT NULL,
                    title    TEXT    NOT NULL,
                    year    INTEGER   NOT NULL,
                    summary    TEXT    NOT NULL,
                    runtime     INTEGER    NOT NULL,
                    rating     REAL     NOT NULL,
                    price     REAL     NOT NULL,
                    FOREIGN KEY (customer_id) REFERENCES customer(id)
                );""")
    
    @staticmethod
    def insert_customer(conn: sqlite3.Connection, name: str, username: str, password: str, address: str) -> None:
        with conn:
            conn.execute("""
                INSERT INTO customer (name, username, password, address)
                VALUES (?, ?, ?, ?)
            """, (name, username, password, address))
            