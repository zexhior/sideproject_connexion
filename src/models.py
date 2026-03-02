from sqlalchemy import DateTime, String, Integer, BigInteger, MetaData, ForeignKey, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from config import PG_SCHEMA
from base import Base
  
class Person(Base):
  __tablename__ = 'person'
  
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  nom: Mapped[str]=mapped_column(String(255))
  adresse: Mapped[str] = mapped_column(String(255))
  date_naissance: Mapped[DateTime] = mapped_column(DateTime)
  cin: Mapped[str]=mapped_column(String(255))
  
class Transaction(Base):
  __tablename__ = 'transaction'
  
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  montant: Mapped[float] = mapped_column(BigInteger)
  date_transaction: Mapped[DateTime] = mapped_column(DateTime)
  person_id: Mapped[int] = mapped_column(Integer, ForeignKey('person.id'))