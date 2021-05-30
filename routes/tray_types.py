from fastapi import APIRouter
from src.db_interface import get_trays
from src.utils import get_db_path


router = APIRouter(
    prefix="/tray_types",
    tags=["tray_types"],
    responses={404: {"description": "Not found"}},
)


@router.get('/all')
async def read_items() -> dict:
    """
    Returns all plant entries in the database
    """
    return get_trays(db_path=get_db_path())