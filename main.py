from fastapi import FastAPI
from routers import itinerary
from database import init_db

app = FastAPI()
init_db()
app.include_router(itinerary.router)
