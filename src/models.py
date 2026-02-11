from sqlalchemy import DateTime, String, Integer, Date, BigInteger, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from config import PG_SCHEMA

class Base(DeclarativeBase):
  metadata = MetaData(schema=PG_SCHEMA)
  
class Person(Base):
  __tablename__ = 'person'
  
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  nom: Mapped[str]=mapped_column(String(255))
  adresse: Mapped[str] = mapped_column(String(255))
  date_naissance: Mapped[DateTime] = mapped_column(DateTime)
  cin: Mapped[str]=mapped_column(String(255))