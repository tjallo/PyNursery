import sqlite3
from sqlite3.dbapi2 import Connection, Cursor
from typing import List
from src.plant_metadata import Tray


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


