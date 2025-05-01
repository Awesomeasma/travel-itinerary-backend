One-Pager Document:

Steps Followed to Complete the Assignment:
Step 1: Environment setup by installing necessary dependencies (FastAPI, SQLAlchemy, etc.).

Step 2: Designed and implemented the database schema using SQLAlchemy for storing itineraries, activities, hotels, etc.

Step 3: Created RESTful API endpoints for creating and viewing itineraries.

Step 4: Implemented MCP server for recommending itineraries based on user input (number of nights).

Step 5: Tested the API and MCP server locally (e.g., using http://localhost:8000/itineraries and http://localhost:8001/recommend?nights=3).

----------------------------------------------------------------------------------------------------------

Key Decisions Made During Implementation:
API Framework: Chose FastAPI for building the API because it's fast, easy to use, and has built-in support for validation.

Database: Used SQLAlchemy for managing database models and relationships.

Seeded Data: Focused on Phuket and Krabi regions, simulating real itineraries for 2-8 nights.

----------------------------------------------------------------------------------------------------------

Assumptions Made:
Nights Range: Assumed itineraries would be in the range of 2 to 8 nights based on the problem description.

MCP Recommendations: Assumed that the MCP server should return only one recommended itinerary per request (based on number of nights).

----------------------------------------------------------------------------------------------------------

Challenges Faced and How They Were Resolved:

I didn't face any technical challenges in this assignment. I used SQLAlchemy's relationship fields and foreign keys properly to avoid any database related issues. And i made sure to validate APIs by testing them, and i used Pydantic library in FastAPI for validation purposes.


Github link: https://Awesomeasma/travel-itinerary-backend
Video Demo link: https://drive.google.com/file/d/1kO-3thEXcf5WtngxK5LFZAGKNJ4kj7xl/view?usp=sharing
