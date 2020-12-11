from peewee import PostgresqlDatabase
from config import POSTGRES_USER, POSTGRES_DB, POSTGRES_PORT, POSTGRES_PW, POSTGRES_HOST

db = PostgresqlDatabase(
    POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PW,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT
)
