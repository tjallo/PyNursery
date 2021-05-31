from typing import List
from fastapi import APIRouter, status
from starlette.status import HTTP_201_CREATED, HTTP_405_METHOD_NOT_ALLOWED
from src.db_interface import get_plant_families, add_plant_family, delete_plant_family
from src.utils import get_db_path
from src.plant_metadata import Plant, PlantFamily
from pydantic import BaseModel


router = APIRouter(
    prefix="/plant_families",
    tags=["plant_families"],
    responses={404: {"description": "Not found"}},
)


class PlantFamilyModel(BaseModel):
    """
    Class to supply documentation for the api
    """
    family_name: str

    def toPlantFamily(self) -> PlantFamily:
        """
        Parses JSON-Like PlantFamilyModel Object to PlantFamily Object
        """
        return PlantFamily(self.family_name)



class PlantFamiliesModel(BaseModel):
    """
    Class to supply documentation for the api
    """
    family_names: List[PlantFamilyModel]
    

@router.get('/all')
async def read_items() -> dict:
    """
    Returns all plant_families entries in the database
    """
    return get_plant_families(db_path=get_db_path())


@router.post('/add')
async def post_plant_family(plant_family: PlantFamilyModel):
    """
    Add plant family to the database
    """
    try:
        add_plant_family(get_db_path(), plant_family.toPlantFamily())
        return status.HTTP_201_CREATED
    except:
        return status.HTTP_405_METHOD_NOT_ALLOWED

@router.post('/delete')
async def post_delete_plant_families(plant_families: PlantFamiliesModel):
    """
    Delete list of plant families from the database
    """
    try:
        for family in plant_families.family_names:
            fam: PlantFamily = family.toPlantFamily()
            delete_plant_family(get_db_path(), fam)
        return HTTP_201_CREATED
    except:
        return HTTP_405_METHOD_NOT_ALLOWED
