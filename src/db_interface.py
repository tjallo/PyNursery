import ast
from datetime import datetime
from json import loads
import sqlite3
from sqlite3.dbapi2 import Connection, Cursor
from typing import List
from src.plant_metadata import Climate, Location, Plant, PlantFamily, Tray, PlantBatch


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


def delete_plant(db_path: str, plant: Plant) -> None:
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


def parse_batch_db_entry(row) -> PlantBatch:
    """
    Parses database row of plant batch

    Returns PlantBatch Object
    """

    # We need to reassign to a new variable since dicts are immutable
    print(row)
    row0 = ast.literal_eval(row[0])
    row1 = ast.literal_eval(row[1])
    row2 = ast.literal_eval(row[2])

    plant: Plant = Plant(name=row0['name'], family_name=row0['family_name'], metadata=row0['metadata'])
    location: Location = Location(row1['name'], row1['area'], Climate(row1['climate_type']))
    tray: Tray = Tray(row2['tray_type'], row2['footprint'], row2['capacity'])
    n_trays: int = int(row[3])
    planting_time: datetime = datetime.fromisoformat(row[4])

    batch: PlantBatch = PlantBatch(plant, location, tray, n_trays, planting_time)

    return batch


def parse_plant_location_tray_to_dict(plant_batch: PlantBatch):
    """
    Splits and parses PlantBatch object to Plant, Location and Tray objects

    Args:
        plant_batch (PlantBatch): plant_batch to be converted
    Returns:
        plant (Plant): plant information from plant_batch
        location (Location): location information from plant_batch
        tray (Tray): tray information from plant_batch
    """
    plant: dict = {
        'name': plant_batch.plant.name,
        'family_name': plant_batch.plant.family_name,
        'metadata': plant_batch.plant.metadata
    }

    location: dict = {
        'name': plant_batch.location.name,
        'climate_type': plant_batch.location.climate.climate_type,
        'area': plant_batch.location.area
    }

    tray: dict = {
        'tray_type': plant_batch.tray_type.tray_type,
        'capacity': plant_batch.tray_type.capacity,
        'footprint': plant_batch.tray_type.footprint
    }

    return plant, location, tray


def add_plant_batch(db_path: str, plant_batch: PlantBatch) -> None:
    """
    Add plant batch to the database

    Args:
        db_path (str): string of the location of the DB folder
        plant_batch (PlantBatch): plant that needs to be added to the database
    """
    plant, location, tray = parse_plant_location_tray_to_dict(plant_batch)

    query = f'INSERT INTO batches (Plant, Location, Tray, n_trays, planting_time) VALUES ("{plant}", "{location}", "{tray}", {plant_batch.n_tray}, "{plant_batch.planting_time.isoformat()}")'

    conn: Connection = sqlite3.connect(f'{db_path}\\batches.db')
    curr: Cursor = conn.cursor()
    try:
        curr.execute(query)
    except sqlite3.IntegrityError:
        raise ValueError("Error occured")

    conn.commit()
    curr.close()
    conn.close()


def delete_plant_batch(db_path: str, plant_batch: PlantBatch) -> None:
    """
    Delete plant batch from the database

    Args:
        db_path (str): string of the location of the DB folder
        plant_batch (PlantBatch): plant batch to be removed 
    """
    plant, location, tray = parse_plant_location_tray_to_dict(plant_batch)

    conn: Connection = sqlite3.connect(f'{db_path}\\batches.db')
    curr: Cursor = conn.cursor()
    try:
        curr.execute(f"DELETE FROM batches WHERE (Plant=? AND Tray=? AND Location=? AND planting_time=?)", (str(plant), str(tray), str(location), plant_batch.planting_time.isoformat(),))
    except sqlite3.IntegrityError:
        raise ValueError("There was an error")

    conn.commit()
    curr.close()
    conn.close()


def get_plant_batches(db_path: str) -> List[PlantBatch]:
    """
    Returns list of plant_batches that are in the database

    Args:
        db_path (str): string of the location of the DB folder
    Returns:
        plant_batches (List[PlantBatch]): list of plant batches in database
    """
    plant_batches: List[PlantBatch] = []

    conn: Connection = sqlite3.connect(f'{db_path}\\batches.db')
    cur: Cursor = conn.cursor()

    for row in cur.execute('SELECT Plant, Location, Tray, n_trays, planting_time FROM batches'):
        # print('\n\n')
        # for i in row:
        # print(f"{type(i)}: {i}")

        batch: PlantBatch = parse_batch_db_entry(row)

        plant_batches.append(batch)

    cur.close()
    conn.close()
    return plant_batches


def get_db_count(db_path: str, db_name: str, db_table: str) -> int:
    """
    Returns the count of the number of elements in a table from a certain DB

    Args:
        db_path (str): path of the database
        db_name (str): name of the database you want to acces (e.g. 'company_data.db')
        db_table (str): name of the table you want the count from
    Returns:
        db_count (int): Number of rows in the table

    """
    conn: Connection = sqlite3.connect(f'{db_path}\\{db_name}')
    cur: Cursor = conn.cursor()

    try:
        fetch: List = cur.execute(f'SELECT COUNT(*) FROM {db_table}').fetchall()
        count: int = int(fetch[0][0])
    except:
        count: int = 0

    cur.close()
    conn.close()

    return count


def get_location_stats(db_path: str) -> int:
    """
    Returns the number of entries in the location database

    Args:
        db_path (str): string of the location of the DB folder
    Returns:
        n_locations (int): number of location entries in the database
    """

    return get_db_count(db_path, 'company_data.db', 'locations')


def get_plant_batch_stats(db_path: str) -> int:
    """
    Returns the number of entries in the plant_batch database

    Args:
        db_path (str): string of the location of the DB folder
    Returns:
        n_plant_batches (int): number of plant_batch entries in the database
    """
    return get_db_count(db_path, 'batches.db', 'batches')


def get_plant_family_stats(db_path: str) -> int:
    """
    Returns the number of entries in the plant_family database

    Args:
        db_path (str): string of the location of the DB folder
    Returns:
        n_plant_families (int): number of plant family entries in the database
    """
    return get_db_count(db_path, 'company_data.db', 'plant_families')


def get_plant_stats(db_path: str) -> int:
    """
    Returns the number of entries in the plant database

    Args:
        db_path (str): string of the location of the DB folder
    Returns:
        n_plants (int): number of plant entries in the database
    """
    return get_db_count(db_path, 'company_data.db', 'plants')


def get_tray_type_stats(db_path: str) -> int:
    """
    Returns the number of entries in the tray_type database

    Args:
        db_path (str): string of the location of the DB folder
    Returns:
        n_tray_types (int): number of Tray_type entries in the database
    """
    return get_db_count(db_path, 'company_data.db', 'tray_types')
