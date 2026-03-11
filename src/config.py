from sqlalchemy.engine import URL
from env import PG_HOST, PG_PORT, PG_DB, PG_USER, PG_PASSWORD, PG_SCHEMA, PG_CREATE_SCHEMA

print(f"Configuration: PG_HOST={PG_HOST}, PG_PORT={PG_PORT}, PG_DB={PG_DB}, PG_USER={PG_USER}, PG_SCHEMA={PG_SCHEMA}, PG_CREATE_SCHEMA={PG_CREATE_SCHEMA}")
url_postgres = URL.create(
	drivername="postgresql+psycopg",
	username=PG_USER,
	password=PG_PASSWORD,
	host=PG_HOST,
	port=PG_PORT,
	database=PG_DB,
)