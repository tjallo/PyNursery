from datetime import datetime
from src.utils import get_db_path
from src.db_interface import add_plant, add_tray, delete_location, delete_plant, delete_tray, add_plant_batch, get_plant_batches
from src.plant_metadata import Location, Climate, Plant, PlantBatch, Tray


tray: Tray = Tray('d104', 0.3 * 0.51, 100)
location: Location = Location('Kas', 1400, Climate(2))
plant: Plant = Plant("Test", {}, "Je moeder")

plant_batch: PlantBatch = PlantBatch(plant, location, tray, 30)


add_plant_batch(get_db_path(), plant_batch)

print(get_plant_batches(get_db_path()))
