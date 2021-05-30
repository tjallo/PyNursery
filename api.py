from fastapi import FastAPI

from routes import locations, plant_families, plants, tray_types

app = FastAPI()

app.include_router(locations.router)
app.include_router(plant_families.router)
app.include_router(plants.router)
app.include_router(tray_types.router)


@app.get("/")
async def root():
    """
    Returns Hello World, used as a check if the system is online
    """
    return {"message": "Hello World"}
