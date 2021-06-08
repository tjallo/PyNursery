from typing import Any
from fastapi import APIRouter, status
from pydantic.main import BaseModel
from src.db_interface import get_location_stats, get_plant_stats, get_tray_type_stats, get_plant_batch_stats, get_plant_family_stats
from src.utils import get_db_path

router = APIRouter(
    prefix="/statistics",
    tags=["statistics"],
    responses={404: {"description": "Not found"}},
)


class StatModel(BaseModel):
    """
    BaseModel for the return type of the statistics api
    """
    name: str
    count: int


@router.get('/locations')
def locations_stats() -> StatModel:
    """
    Returns all statistics about the Loaction database
    """
    try:
        count = get_location_stats(get_db_path())
        model = StatModel(name="Locations", count=count)
        return model
    except:
        return status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE


@router.get('/plant_batches')
def plant_batches_stats() -> StatModel:
    """
    Returns all statistics about the Plant Batches database
    """
    try:
        count = get_plant_batch_stats(get_db_path())
        model = StatModel(name="Plant Batches", count=count)
        return model
    except:
        return status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE


@router.get('/plant_families')
def plant_families_stats() -> StatModel:
    """
    Returns all statistics about the Plant Families database
    """
    try:
        count = get_plant_family_stats(get_db_path())
        model = StatModel(name="Plant Families", count=count)
        return model
    except:
        return status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE


@router.get('/plants')
def plant_stats() -> StatModel:
    """
    Returns all statistics about the Plants database
    """
    try:
        count = get_plant_stats(get_db_path())
        model = StatModel(name="Plants", count=count)
        return model
    except:
        return status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE


@router.get('/tray_types')
def tray_type_stats() -> StatModel:
    """
    Returns all statistics about the tray_types Families database
    """
    try:
        count = get_tray_type_stats(get_db_path())
        model = StatModel(name="Tray Types", count=count)
        return model
    except:
        return status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
