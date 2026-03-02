from datetime import datetime
from sqlalchemy import DateTime, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from env import PG_SCHEMA

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    metadata = MetaData(schema=PG_SCHEMA)