from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from app.main.core.config import Config

#DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URI = "postgresql://mvondofernando7777:jarodak47@localhost:5432/hotel"

engine = create_engine(Config.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)





