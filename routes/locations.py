from typing import List
from fastapi import APIRouter, status
from src.plant_metadata import Location, Climate
from src.db_interface import add_location, delete_location, get_locations
from src.utils import get_db_path
from pydantic import BaseModel, parse
from traceback import print_exc


router = APIRouter(
    prefix="/locations",
    tags=["locations"],
    responses={404: {"description": "Not found"}},
)


class LocationModel(BaseModel):
    name: str
    area: float
    climate_type: int

class LocationsModel(BaseModel):
    locations: List[LocationModel]

def parse_location_model(location: LocationModel) -> Location:
    """
    Parses JSON-like LocationModel object to Location object
    """
    return Location(str(location.name), float(location.area), Climate(int(location.climate_type)))


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
        l1 = parse_location_model(location)
        add_location(get_db_path(), l1)
        return status.HTTP_201_CREATED
    except:
        print_exc()
        return status.HTTP_405_METHOD_NOT_ALLOWED


@router.post('/delete')
async def post_delete_locations(locations: LocationsModel):
    print(locations)
    try:
        for location in locations.locations:
            l1 = parse_location_model(location)
            delete_location(get_db_path(), l1)
        return status.HTTP_201_CREATED
    except:
        print_exc()
        return status.HTTP_405_METHOD_NOT_ALLOWED
    

