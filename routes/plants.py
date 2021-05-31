from typing import List
from fastapi import APIRouter, status
from src.db_interface import add_plant, get_plants
from src.plant_metadata import Plant
from src.utils import get_db_path
from pydantic import BaseModel



router = APIRouter(
    prefix="/plants",
    tags=["plants"],
    responses={404: {"description": "Not found"}},
)


class PlantModel(BaseModel):
    """
    Class to supply documentation for the api
    """
    name: str
    family_name: str


    def toPlant(self) -> Plant:
        """
        Parses JSON-Like PlantModel Object to Plant Object
        """
        return Plant(self.family_name, {}, self.name)


class PlantsModel(BaseModel):
    """
    Class to supply documentation for the api
    """
    plants: List[Plant]


@router.get('/all')
async def read_items() -> dict:
    """
    Returns all plant entries in the database
    """
    return get_plants(db_path=get_db_path())


@router.post('/add')
async def post_plant(plant: PlantModel):
    """
    Add plant to the database
    """
    try:
        add_plant(get_db_path(), plant.toPlant())
        return status.HTTP_201_CREATED
    except:
        return status.HTTP_405_METHOD_NOT_ALLOWED


@router.post('/delete')
async def post_delete_plant(plants: Plant):
    """
    Delete list of plants from the database
    """
    print(plants)