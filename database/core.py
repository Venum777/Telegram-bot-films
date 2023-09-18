import psycopg2


class Connection:
    """
    Connection with PosgreSQL
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(
                Connection, cls
            ).__new__(cls)
        return cls.instance

    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: str,
        dbname: str
    ) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname
        self.conn = None
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                dbname=self.dbname
            )
            self.conn.autocommit = True
            print('[SUCCESS] Connection is success!')
        except Exception as e:
            print(e)
            print("[ERROR] CONNECTION ERROR!")

    def create_tables(self) -> None:
        try:
            with self.conn.cursor() as cur:
                cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS genres(
            id SERIAL PRIMARY KEY,
            name VARCHAR(60) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS films(
            id SERIAL PRIMARY KEY,
            title VARCHAR(120) UNIQUE NOT NULL,
            heading TEXT NOT NULL,
            genre_id INTEGER REFERENCES genres(id) NOT NULL,
            date_publication TIMESTAMP DEFAULT(NOW()),
            rate INTEGER DEFAULT(1)
        );
        '''
    )
        except:
            print('[ERROR] CAN CREATE TABLES')
