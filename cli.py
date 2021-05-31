from src.utils import get_db_path
from src.db_interface import add_plant, delete_location, delete_plant
from src.plant_metadata import Location, Climate, Plant


p1 = Plant('test', {}, "je moeder")
p2 = Plant('test2', {}, "123je moeder")
p3 = Plant('test3', {}, "345je moeder")


# add_plant(get_db_path(), p1)
# add_plant(get_db_path(), p2)
# add_plant(get_db_path(), p3)


delete_plant(get_db_path(), p1)