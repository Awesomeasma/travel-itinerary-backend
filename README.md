- Install libraries:
 
pip install fastapi uvicorn sqlalchemy pydantic

-------------------------------------------------------------------------------------------------------------

- Seed the database:
- This sets up our SQLite database and populates it with sample data:

python seed_data.py

-------------------------------------------------------------------------------------------------------------

- Start the main FastAPI server (port 8000):

uvicorn main:app --reload

Now go to: http://localhost:8000/docs (We can test APIs here)

Endpoint to create a new itinerary:
POST http://localhost:8000/itinerary

Endpoint to view all itineraries:
GET http://localhost:8000/itineraries

-------------------------------------------------------------------------------------------------------------

Start the MCP Server for itinerary recommendations (port 8001):

uvicorn mcp_server:app --port 8001 --reload

Endpoint to get recommendations by number of nights:
GET http://localhost:8001/recommend?nights=3

-------------------------------------------------------------------------------------------------------------
