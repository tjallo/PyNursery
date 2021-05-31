from typing import List
from fastapi import APIRouter, status
from src.db_interface import get_trays, add_tray, delete_tray
from src.utils import get_db_path
from src.plant_metadata import Tray
from pydantic import BaseModel


router = APIRouter(
    prefix="/tray_types",
    tags=["tray_types"],
    responses={404: {"description": "Not found"}},
)


class TrayModel(BaseModel):
    """
    Class to supply documentation for the api
    """
    tray_type: str
    capacity: int
    footprint: float

    def toTray(self) -> Tray:
        """
        Parses JSON-Like TrayModel Object to Tray Object
        """
        return Tray(self.tray_type, self.footprint, self.capacity)


class TraysModel(BaseModel):
    """
    Class to supply documentation for the api
    """
    trays: List[TrayModel]


@router.get('/all')
async def read_items() -> dict:
    """
    Returns all plant entries in the database
    """
    return get_trays(db_path=get_db_path())


@router.post('/add')
async def post_tray(tray: TrayModel):
    """
    Add tray to the database
    """
    try:
        add_tray(get_db_path(), tray.toTray())
        return status.HTTP_201_CREATED
    except:
        return status.HTTP_405_METHOD_NOT_ALLOWED


@router.post('/delete')
async def post_delete_tray(trays: TraysModel):
    """
    Delete list of trays from the database
    """
    try:
        for tray in trays.trays:
            delete_tray(get_db_path(), tray.toTray())
        return status.HTTP_201_CREATED
    except:
        return status.HTTP_405_METHOD_NOT_ALLOWED
