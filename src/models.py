from sqlalchemy import DateTime, String, Integer, BigInteger, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from config import PG_SCHEMA
from base import Base
  
class Connexion(Base):
  __tablename__ = 'connexion'

  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  source: Mapped[str] = mapped_column(String(100), default='application')
  status: Mapped[str] = mapped_column(String(20))
  checked_at: Mapped[DateTime] = mapped_column(DateTime) 