from datetime import datetime
from src.utils import get_db_path
from src.db_interface import add_plant, add_tray, delete_location, delete_plant, delete_tray
from src.plant_metadata import Location, Climate, Plant, PlantBatch, Tray


tray: Tray = Tray('d104', 0.3 * 0.51, 100)
location: Location = Location('Kas', 1400, Climate(2))
plant: Plant = Plant("Test", {}, "Je moeder")

batch: PlantBatch = PlantBatch(plant, location, tray, 30)

print(f"Age: {batch.get_age()} days")
print(f"Date: {batch.get_plant_date()}")
print(f"Count: {batch.get_plant_count()}")
print(f"Area: {batch.get_area()}m2")
print(f"Timestamp {str(batch.planting_time)}")
dt = str(batch.planting_time)
print(datetime.fromisoformat(dt))