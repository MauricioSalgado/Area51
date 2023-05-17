from sqlalchemy import Column, Integer, String
from database import Base


class Watch(Base):
    __tablename__ = "watches"
    
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String)
    year = Column(String)
    price = Column(Integer)