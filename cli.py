from src.utils import get_db_path
from src.db_interface import delete_location
from src.plant_metadata import Location, Climate


l1 = Location('New Field', 34, Climate(0))
delete_location(get_db_path(), l1)
