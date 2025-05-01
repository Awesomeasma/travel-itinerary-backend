from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Itinerary, Day
from database import SessionLocal
from pydantic import BaseModel
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class DaySchema(BaseModel):
    day_number: int
    hotel: str
    transfer: str
    activity: str

class ItineraryCreate(BaseModel):
    name: str
    nights: int
    days: List[DaySchema]

@router.post("/itinerary")
def create_itinerary(itin: ItineraryCreate, db: Session = Depends(get_db)):
    itinerary = Itinerary(name=itin.name, nights=itin.nights)
    db.add(itinerary)
    db.flush()
    for day in itin.days:
        db.add(Day(itinerary_id=itinerary.id, **day.dict()))
    db.commit()
    return {"message": "Itinerary created", "id": itinerary.id}

@router.get("/itineraries")
def get_itineraries(db: Session = Depends(get_db)):
    return db.query(Itinerary).all()
