from fastapi import APIRouter
from src.db_interface import get_plant_families
from src.utils import get_db_path


router = APIRouter(
    prefix="/plant_families",
    tags=["plant_families"],
    responses={404: {"description": "Not found"}},
)


@router.get('/all')
async def read_items() -> dict:
    """
    Returns all plant_families entries in the database
    """
    return get_plant_families(db_path=get_db_path())