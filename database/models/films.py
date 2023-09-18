# Local
from database.core import Connection


class Film:
    """Object from db. Film."""

    id: int
    title: str
    heading: str
    genre_id: int
    rate: int

    @staticmethod
    def create(
        conn: Connection,
        title: str,
        heading: str,
        genre_id: int,
        rate: int
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO films(
                        title,
                        heading,
                        genre_id,
                        rate
                )
                VALUES (
                    '{title}',
                    '{heading}',
                    '{genre_id}',
                    '{rate}'
                )
                """
            )
    
    @staticmethod
    def get_all(conn: Connection) -> 'Film':

        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT title,heading,genre_id,rate FROM films
                """
            )
            result = cur.fetchall()
            data_list = [row for row in result]
            return data_list
        
    @staticmethod
    def get_all_by_genre(conn: Connection, genre_id: int) -> 'Film':

        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT title,heading,genre_id,rate FROM films WHERE genre_id = {genre_id}
                """
            )
            return cur.fetchall()
        