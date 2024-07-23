from sqlalchemy import Column, Integer, String
from src.database import engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tramit(Base):
    __tablename__ = "tramit"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
