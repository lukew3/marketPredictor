import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class BTCUSDT(Base):
    __tablename__ = 'BTCUSDT'
    id = Column(Integer, primary_key=True)
    datetime = Column(String(250), nullable=False)
    open = Column(Integer)
    close = Column(Integer)
    low = Column(Integer)
    high = Column(Integer)
    volume = Column(Integer)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///priceData.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
