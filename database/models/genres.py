# Local
from database.core import Connection


class Genre:
    """Object from db. Genre."""

    id: int
    name: str

    @staticmethod
    def create(
        conn: Connection,
        name: str,
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO genres(
                    name
                )
                VALUES (
                    '{name}'
                )
                """
            )
    
    @staticmethod
    def get_all(conn: Connection) -> 'Genre':

        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT * FROM genres
                """
            )
            return cur.fetchall()
            