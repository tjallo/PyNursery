from fastapi import APIRouter
from src.db_interface import get_locations
from src.utils import get_db_path


router = APIRouter(
    prefix="/locations",
    tags=["locations"],
    responses={404: {"description": "Not found"}},
)


@router.get('/all')
async def read_items() -> dict:
    """
    Returns all location entries in the database
    """
    return get_locations(db_path=get_db_path())
