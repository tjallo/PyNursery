from src.plant_metadata import Climate, Location
from src.db_interface import add_location, get_locations


DB_PATH = 'C:\\Users\\tjalw\\Documents\\GitHub\\PyNursery\\db'

print(get_locations(DB_PATH))


