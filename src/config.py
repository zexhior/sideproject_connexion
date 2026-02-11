import os, dotenv
from sqlalchemy.engine import URL

dotenv.load_dotenv()

PG_HOST = os.getenv("PG_HOST")
PG_PORT = int(os.getenv("PG_PORT"))
PG_DB = os.getenv("PG_DB")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_SCHEMA = os.getenv("PG_SCHEMA")
PG_CREATE_SCHEMA = os.getenv("PG_CREATE_SCHEMA", "false").lower() in {"1", "true", "yes"}

print(f"Configuration: PG_HOST={PG_HOST}, PG_PORT={PG_PORT}, PG_DB={PG_DB}, PG_USER={PG_USER}, PG_SCHEMA={PG_SCHEMA}, PG_CREATE_SCHEMA={PG_CREATE_SCHEMA}")
url_postgres = URL.create(
	drivername="postgresql+psycopg2",
	username=PG_USER,
	password=PG_PASSWORD,
	host=PG_HOST,
	port=PG_PORT,
	database=PG_DB,
)