from typing import List
from fastapi import APIRouter, status
from src.plant_metadata import Location, Climate
from src.db_interface import add_location, delete_location, get_locations
from src.utils import get_db_path
from pydantic import BaseModel
from traceback import print_exc


router = APIRouter(
    prefix="/locations",
    tags=["locations"],
    responses={404: {"description": "Not found"}},
)


class LocationModel(BaseModel):
    """
    Location model for the API documentation
    """
    name: str
    area: float
    climate_type: int

    def toLocation(self) -> Location:
        """
        Parses JSON-Like LocationModel object to Loaction object
        """
        return Location(str(self.name), float(self.area), Climate(int(self.climate_type)))


class LocationsModel(BaseModel):
    """
    List of LoactionModels for the API documentation
    """
    locations: List[LocationModel]


@router.get('/all')
async def read_locations() -> dict:
    """
    Returns all location entries in the database
    """
    return get_locations(db_path=get_db_path())


@router.post('/add')
async def post_location(location: LocationModel):
    """
    Adds an location to the database
    """
    try:
        add_location(get_db_path(), location.toLocation())
        return status.HTTP_201_CREATED
    except:
        print_exc()
        return status.HTTP_405_METHOD_NOT_ALLOWED


@router.post('/delete')
async def post_delete_locations(locations: LocationsModel):
    """
    Deletes supplies locations from the database
    """
    try:
        for location in locations.locations:
            delete_location(get_db_path(), location.toLocation())
        return status.HTTP_201_CREATED
    except:
        print_exc()
        return status.HTTP_405_METHOD_NOT_ALLOWED
