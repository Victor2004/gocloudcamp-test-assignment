from sqlalchemy import Column, Integer, String
from database import Base
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    service = Column(String(256))
    data = Column(String(256))

class MyserviceDB(Base):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True)
    current_id = Column(String(256))
