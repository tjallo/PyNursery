from typing import List
from src.db_interface import add_plant_family, get_plant_families
from src.plant_metadata import Plant, PlantFamily


DB_PATH = "C:\\Users\\tjalw\\Documents\\GitHub\\PyNursery\\db"


plants: List[str]

with open("C:\\Users\\tjalw\\Documents\\GitHub\\PyNursery\\src\\web_scraper\\latin_names.txt") as file:
    plants = file.readlines()

plants = [x.strip() for x in plants]

for plant in plants:
    p1 = PlantFamily(plant, {})
    add_plant_family(DB_PATH, p1)

print(get_plant_families(DB_PATH))
