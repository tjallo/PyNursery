import sqlite3
from sqlite3.dbapi2 import Connection, Cursor
from typing import List
from src.plant_metadata import Climate, Location, Plant, PlantFamily, Tray


def get_trays(db_path: str) -> List[Tray]:
    """
    Returns list of tray types that are in the database

    Args:
        db_path (str): string of the location of the DB folder

    Returns:
        trays (List[Tray]): Array of all the trays in the database
    """
    trays: List[Tray] = []
    conn: Connection = sqlite3.connect(f'{db_path}\\company_data.db')
    cur: Cursor = conn.cursor()
    for row in cur.execute('SELECT tray_type, footprint, capacity FROM tray_types'):
        trays.append(Tray(row[0], row[1], row[2]))

    cur.close()
    conn.close()
    return trays


def add_tray(db_path: str, tray: Tray) -> None:
    """
    Add tray to tray types the database

    Args:
        db_path (str): string of the location of the DB folder
        tray (Tray): Tray that needs to be added
    """
    query = f'INSERT INTO tray_types (tray_type, capacity, footprint) VALUES ("{tray.tray_type}", {tray.capacity}, {tray.footprint})'

    conn: Connection = sqlite3.connect(f'{db_path}\\company_data.db')
    curr: Cursor = conn.cursor()
    try:
        curr.execute(query)
    except sqlite3.IntegrityError:
        raise ValueError("Error, tray already exists in database.")

    conn.commit()
    curr.close()
    conn.close()


def delete_tray(db_path: str, tray: Tray):
    """
    Remove specific tray from database

    Args:
        db_path (str): string of the location of the DB folder
        location (Location): location to be removed 
    """
    # Since the names need to be unique in the SQL Databse
    # we can filter on the specific name
    query = f"DELETE FROM tray_types WHERE tray_type='{tray.tray_type}'"

    conn: Connection = sqlite3.connect(f'{db_path}\\company_data.db')
    curr: Cursor = conn.cursor()
    try:
        curr.execute(query)
    except sqlite3.IntegrityError:
        raise ValueError("There was an error")

    conn.commit()
    curr.close()
    conn.close()


def get_locations(db_path: str) -> List[Location]:
    """
    Returns list of locations that are in the database

    Args:
        db_path (str): string of the location of the DB folder
    Returns:
        locations (List[Location]): list of all the locations in the database
    """
    locations: List[Location] = []
    conn: Connection = sqlite3.connect(f'{db_path}\\company_data.db')
    cur: Cursor = conn.cursor()
    for row in cur.execute('SELECT name, area, climate FROM locations'):
        locations.append(Location(row[0], row[1], Climate(row[2])))

    cur.close()
    conn.close()
    return locations


def add_location(db_path: str, location: Location) -> None:
    """
    Add location to locations in the database

    Args:
        db_path (str): string of the location of the DB folder
        location (Location): location that needs to be added to the database
    """
    query = f'INSERT INTO locations (name, area, climate) VALUES ("{location.name}", {location.area}, {location.climate.climate_type})'

    conn: Connection = sqlite3.connect(f'{db_path}\\company_data.db')
    curr: Cursor = conn.cursor()
    try:
        curr.execute(query)
    except sqlite3.IntegrityError:
        raise ValueError("Error, tray already exists in database.")

    conn.commit()
    curr.close()
    conn.close()


def delete_location(db_path: str, location: Location):
    """
    Remove specific location from database

    Args:
        db_path (str): string of the location of the DB folder
        location (Location): location to be removed 
    """
    # Since the names need to be unique in the SQL Databse
    # we can filter on the specific name
    query = f"DELETE FROM locations WHERE name='{location.name}'"

    conn: Connection = sqlite3.connect(f'{db_path}\\company_data.db')
    curr: Cursor = conn.cursor()
    try:
        curr.execute(query)
    except sqlite3.IntegrityError:
        raise ValueError("There was an error")

    conn.commit()
    curr.close()
    conn.close()


def get_plant_families(db_path: str) -> List[PlantFamily]:
    """
    Returns list of plant_families that are in the database

    Args:
        db_path (str): string of the location of the DB folder
    Returns:
        plant_families (List[PlantFamily]): list of plant_families in database
    """
    families: List[PlantFamily] = []
    conn: Connection = sqlite3.connect(f'{db_path}\\company_data.db')
    cur: Cursor = conn.cursor()
    for row in cur.execute('SELECT family_name, meta_data FROM plant_families'):
        families.append(PlantFamily(row[0], dict(eval(row[1]))))

    cur.close()
    conn.close()
    return families


def add_plant_family(db_path: str, plant_family: PlantFamily) -> None:
    """
    Add plant_family to plant_families in the database

    Args:
        db_path (str): string of the location of the DB folder
        plant_family (PlantFamily): plant_family that needs to be added to the database
    """
    query = f'INSERT INTO plant_families (family_name, meta_data) VALUES ("{plant_family.family_name}", "{str(plant_family.metadata)}")'

    conn: Connection = sqlite3.connect(f'{db_path}\\company_data.db')
    curr: Cursor = conn.cursor()
    try:
        curr.execute(query)
    except sqlite3.IntegrityError:
        raise ValueError("Error, plant_family already exists in database.")

    conn.commit()
    curr.close()
    conn.close()


def delete_plant_family(db_path: str, plant_family: PlantFamily):
    """
    Delete plant_family from the database

    Args:
        db_path (str): string of the location of the DB folder
        plant_family (PlantFamily): location to be removed 
    """
    # Since the names need to be unique in the SQL Databse
    # we can filter on the specific name
    query = f"DELETE FROM plant_families WHERE family_name='{plant_family.family_name}'"

    conn: Connection = sqlite3.connect(f'{db_path}\\company_data.db')
    curr: Cursor = conn.cursor()
    try:
        curr.execute(query)
    except sqlite3.IntegrityError:
        raise ValueError("There was an error")

    conn.commit()
    curr.close()
    conn.close()


def get_plants(db_path: str) -> List[Plant]:
    """
    Returns list of plants that are in the database

    Args:
        db_path (str): string of the location of the DB folder
    Returns:
        plants (List[Plant]): list of plants in database
    """
    plants: List[Plant] = []
    conn: Connection = sqlite3.connect(f'{db_path}\\company_data.db')
    cur: Cursor = conn.cursor()
    for row in cur.execute('SELECT family_name, metadata, name FROM plants'):
        plants.append(Plant(row[0], dict(eval(row[1])), row[2]))

    cur.close()
    conn.close()
    return plants


def add_plant(db_path: str, plant: Plant) -> None:
    """
    Add plant to plant in the database

    Args:
        db_path (str): string of the location of the DB folder
        plant (Plant): plant that needs to be added to the database
    """
    query = f'INSERT INTO plants (name, family_name, metadata) VALUES ("{plant.name}", "{plant.family_name}", "{str(plant.metadata)}")'

    conn: Connection = sqlite3.connect(f'{db_path}\\company_data.db')
    curr: Cursor = conn.cursor()
    try:
        curr.execute(query)
    except sqlite3.IntegrityError:
        raise ValueError("Error, plant_family already exists in database.")

    conn.commit()
    curr.close()
    conn.close()


def add_plant(db_path: str, plant: Plant) -> None:
    """
    Add plant to plants in the database

    Args:
        db_path (str): string of the location of the DB folder
        plant (Plant): plant that needs to be added to the database
    """
    query = f'INSERT INTO plants (name, family_name, metadata) VALUES ("{str(plant.name)}", "{str(plant.family_name)}", "{str(plant.metadata)}")'

    conn: Connection = sqlite3.connect(f'{db_path}\\company_data.db')
    curr: Cursor = conn.cursor()
    try:
        curr.execute(query)
    except sqlite3.IntegrityError:
        raise ValueError("Error, plant already exists in database.")

    conn.commit()
    curr.close()
    conn.close()


def delete_plant(db_path: str, plant: Plant):
    """
    Delete plant from the database

    Args:
        db_path (str): string of the location of the DB folder
        plant (Plant): plant to be removed 
    """
    # Since the names need to be unique in the SQL Databse
    # we can filter on the specific name
    query = f"DELETE FROM plants WHERE name='{plant.name}'"

    conn: Connection = sqlite3.connect(f'{db_path}\\company_data.db')
    curr: Cursor = conn.cursor()
    try:
        curr.execute(query)
    except sqlite3.IntegrityError:
        raise ValueError("There was an error")

    conn.commit()
    curr.close()
    conn.close()


def get_plants(db_path: str) -> List[Plant]:
    """
    Returns list of plants that are in the database

    Args:
        db_path (str): string of the location of the DB folder
    Returns:
        plants (List[Plant]): list of plants in database
    """
    plants: List[Plant] = []
    conn: Connection = sqlite3.connect(f'{db_path}\\company_data.db')
    cur: Cursor = conn.cursor()
    for row in cur.execute('SELECT family_name, metadata, name FROM plants'):
        plants.append(Plant(row[0], dict(eval(row[1])), row[2]))

    cur.close()
    conn.close()
    return plants
