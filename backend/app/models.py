from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for all models
Base = declarative_base()

# Model for the 'duas' table


class Dua(Base):
    __tablename__ = "duas"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
