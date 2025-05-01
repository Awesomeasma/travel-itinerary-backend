from database import SessionLocal, init_db
from models import Itinerary, Day

init_db()
db = SessionLocal()

# Add sample itinerary
itinerary = Itinerary(name="Phuket 3 Nights", nights=3)
db.add(itinerary)
db.flush()

# Add days
days = [
    Day(itinerary_id=itinerary.id, day_number=1, hotel="Phuket Hotel A", transfer="Airport to Hotel", activity="Beach Visit"),
    Day(itinerary_id=itinerary.id, day_number=2, hotel="Phuket Hotel A", transfer="--", activity="Island Hopping"),
    Day(itinerary_id=itinerary.id, day_number=3, hotel="Phuket Hotel A", transfer="--", activity="Shopping"),
]

db.add_all(days)
db.commit()
print("Seed complete!")
