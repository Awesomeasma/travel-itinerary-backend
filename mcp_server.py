from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Itinerary

app = FastAPI()

@app.get("/recommend")
def recommend_itinerary(nights: int):
    db: Session = SessionLocal()
    result = db.query(Itinerary).filter(Itinerary.nights == nights).first()
    if not result:
        return {"message": "No recommendation found"}
    return {
        "id": result.id,
        "name": result.name,
        "nights": result.nights
    }
