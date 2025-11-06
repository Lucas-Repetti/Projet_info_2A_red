import psycopg2
import psycopg2.extras
from contextlib import contextmanager


class DBConnection:
    """
    Classe utilitaire gérant la connexion à la base PostgreSQL.
    Utilisée comme un gestionnaire de contexte ("with DBConnection().connection as conn:").
    """

    def __init__(
        self,
        host: str = "localhost",
        dbname: str = "projet_info",
        user: str = "postgres",
        password: str = "postgres",
        port: int = 5432,
    ):
        self.connection_params = {
            "host": host,
            "dbname": dbname,
            "user": user,
            "password": password,
            "port": port,
        }

    @property
    @contextmanager
    def connection(self):
        """
        Fournit une connexion PostgreSQL utilisable dans un bloc 'with'.
        Gère automatiquement le commit / rollback et la fermeture.
        """
        conn = None
        try:
            # Connexion avec dict cursor (résultats sous forme de dicts)
            conn = psycopg2.connect(**self.connection_params)
            with conn.cursor() as cursor:
                cursor.execute("SET search_path TO projet;")
            yield conn
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"[ERREUR DB] {e}")
            raise
        finally:
            if conn:
                conn.close()
