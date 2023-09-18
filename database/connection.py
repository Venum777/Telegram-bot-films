from database.core import Connection


my_connection: Connection = Connection(
    host='localhost',
    port=5432,
    user='postgres',
    password='admin',
    dbname='Films'
)
