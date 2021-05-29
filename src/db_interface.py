import sqlite3
from sqlite3.dbapi2 import Connection, Cursor
from typing import List
from src.plant_metadata import Climate, Location, Tray


def get_trays(db_path: str) -> List[Tray]:
    """
    Returns list of tray types that are in the database
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


def get_locations(db_path: str) -> List[Location]:
    """
    Returns list of locations that are in the database
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
