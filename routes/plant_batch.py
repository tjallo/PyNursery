from typing import List
from fastapi import APIRouter, status
from pydantic import BaseModel
from src.plant_metadata import PlantBatch, Plant, Location, Tray
from src.db_interface import add_plant_batch, delete_plant_batch, get_plant_batches
from src.utils import get_db_path
from datetime import datetime
import traceback


router = APIRouter(
    prefix="/plant_batch",
    tags=["plant_batch"],
    responses={404: {"description": "Not found"}},
)


class PlantBatchModel(BaseModel):
    """
    PlantBatch model for API Documentation
    """
    plant: Plant
    location: Location
    tray_type: Tray
    n_trays: int
    planting_time: datetime

    def toPlantBatch(self):
        """
        Returns PlantBatch Object from Model
        """
        return PlantBatch(self.plant, self.location, self.tray_type, self.n_trays, self.planting_time)


class PlantBatchesModel(BaseModel):
    """
    PlantBatches model for api Documentation
    """
    plant_batches: List[PlantBatchModel]


@router.get('/all')
async def read_items() -> List[PlantBatch]:
    """
    Returns all plant batch entries in the database
    """
    return get_plant_batches(db_path=get_db_path())


@router.post('/add')
async def post_plant_batch(plant_batch: PlantBatchModel):
    """
    Add plant_batch to the database
    """
    try:
        add_plant_batch(get_db_path(), plant_batch.toPlantBatch())
        return status.HTTP_201_CREATED
    except :
        traceback.print_exc()
        return status.HTTP_405_METHOD_NOT_ALLOWED


@router.post('/delete')
async def post_delete_plant_batch(plant_batches: PlantBatchesModel):
    """
    Delete list of trays from the database
    """
    try:
        for plant_batch in plant_batches.plant_batches:
            delete_plant_batch(get_db_path(), plant_batch.toPlantBatch())
        return status.HTTP_201_CREATED
    except:
        return status.HTTP_405_METHOD_NOT_ALLOWED
