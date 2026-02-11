from sqlalchemy import create_engine, text
from config import url_postgres, PG_SCHEMA, PG_CREATE_SCHEMA

engine = create_engine(url_postgres)

from models import Base

# if PG_CREATE_SCHEMA and PG_SCHEMA != "public":
# 	if not PG_SCHEMA.replace("_", "").isalnum():
# 		raise ValueError("Invalid schema name")
# 	with engine.begin() as connection:
# 		connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS {PG_SCHEMA}"))

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()