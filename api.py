from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import locations, plant_families, plants, tray_types, plant_batch, statistics

app = FastAPI()

# Destructuring routes to different files for cleanliness
# Router Imports
app.include_router(locations.router)
app.include_router(plant_families.router)
app.include_router(plants.router)
app.include_router(tray_types.router)
app.include_router(plant_batch.router)
app.include_router(statistics.router)

# Only alow from these origins to prevent people from outside your network to access your API
origins = [
    "http://localhost",
    "http://localhost:8080",
]

# Adding middelware to allow for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    Returns Hello World, used as a check if the system is online
    """
    return {"message": "Hello World, I am online and functioning!"}
