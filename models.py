from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Itinerary(Base):
    __tablename__ = "itineraries"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    nights = Column(Integer)
    days = relationship("Day", back_populates="itinerary")

class Day(Base):
    __tablename__ = "days"
    id = Column(Integer, primary_key=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"))
    day_number = Column(Integer)
    hotel = Column(String)
    transfer = Column(String)
    activity = Column(String)
    
    itinerary = relationship("Itinerary", back_populates="days")
