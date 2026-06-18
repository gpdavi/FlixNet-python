import sqlite3
class CustomerArchive:

    def connection(way_db: str = "custumer.db") -> sqlite3.Connection:
        #Cria e retorna uma conexão com o banco de dados.
        conn = sqlite3.connect(way_db)
        conn.row_factory = sqlite3.Row   # resultados acessíveis por nome de coluna
        conn.execute("PRAGMA foreign_keys = ON")  # ativa chaves estrangeiras
        return conn
    
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
                CREATE TABLE IF NOT EXISTS cart (
                    id      INTEGER PRIMARY KEY AUTOINCREMENT,
                    title    TEXT    NOT NULL,
                    year    INTEGER   NOT NULL,
                    summary    TEXT    NOT NULL,
                    runtime     INTEGER    NOT NULL,
                    rating     REAL     NOT NULL,
                    price     REAL     NOT NULL
                );""")
            
            