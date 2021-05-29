from dataclasses import dataclass
from typing import List

from PyQt5 import QtCore
from src.utils import is_valid_name
from datetime import datetime


@dataclass(repr=True)
class PlantFamily():
    """
    Dataclass for storing PlantFamily information

    Note: 
    The @dataclass module provides a decorator and functions for automatically adding generated special methods
    such as __init__() and __repr__() to user-defined classes. 
    It was originally described in PEP 557: https://docs.python.org/3/library/dataclasses.html

    The dataclass decorator will be used troughout this project.
    """
    family_name: str
    metadata: dict

    def __init__(self, family_name: str, metadata: dict = {}) -> None:
        """
        Constructor for PlantFamily

        Args:
            family_name (str): Alphanumeric family-name
            metadata (dict): metadata for the FamilyName (e.g. growthtime or other specifics for this plantfamily-type)
        Returns:
            None
        """
        if is_valid_name(family_name) and type(metadata) == dict:
            self.family_name = family_name
            self.metadata = metadata
        else:
            raise ValueError("Please enter a valid family name and/or valid metadata")


@dataclass(repr=True)
class Plant(PlantFamily):
    """
    Class for sepcific plants
    """
    name: str

    def __init__(self, family_name: str, metadata: dict, name: str) -> None:
        """
        Args: 
            family_name (str): Alphanumeric family-name
            metadata (dict): metadata for the FamilyName (e.g. growthtime or other specifics for this plantfamily-type)
            name(str): name of the plant

        """
        super().__init__(family_name, metadata=metadata)
        if is_valid_name(name):
            self.name = name
        else:
            raise ValueError("Please enter a valid plant name")


@dataclass(repr=True)
class Climate:
    """
    Used to compare certain climates and get meta-data 

    Consists of 3 types of climates
        - 2, Greenhouse (Hottest)
        - 1, Hoophouse (Insulated, but not as hot as the greenhouse)
        - 0, Field (Standing outside, or planted on the field)
    """
    climate_type: int
    climate_name: str

    def __init__(self, climate_type: int) -> None:
        """
        Constructor

        Args:
            climate_type (int): Consists of 3 types of climates
            - 2, Greenhouse (Hottest)
            - 1, Hoophouse (Insulated, but not as hot as the greenhouse)
            - 0, Field (Standing outside, or planted on the field)
        """
        if (climate_type >= 0 and climate_type <= 2):
            self.climate_type: int = climate_type
            self.climate_name: str = ['Field', 'Hoophouse', 'Greenhouse'][climate_type]
        else:
            raise ValueError("Please enter a valid climatetype")


@dataclass(repr=True)
class Location():
    """
    Dataclass to store location info

    Among the information is name of the location, area of the location (in m^2), and the Climate of the location.
    """
    name: str
    area: float
    climate: Climate

    def __init__(self, name: str, area: float, climate: Climate) -> None:
        """
        Constructor

        Args:
            name (str): name of the location (should be alphanumeric)
            area (float): m^2 size of the location
            climate (Climate): climate of the location
        """

        if is_valid_name(name) and area > 0 and type(climate) == Climate:
            self.name = name
            self.area = area
            self.climate = climate
        else:
            raise ValueError("Make sure you have entered valid datatypes for each parameter.")


@dataclass(repr=True)
class Tray:
    """
    Used to differentiate between different tray types 
    and sizes
    """
    tray_type: str
    footprint: float
    capacity: int

    def __init__(self, tray_type: str, footprint: float, capacity: int) -> None:
        """
        Type of tray that is used

        Args:
            tray_type (str): codename of the traytype, alphanumeric, without spaces
            footprint (float): size in m^2 that the tray takes up
            capacity (int): number of plants/cuttings tray can accomodate
        """
        if tray_type.isalnum() and footprint > 0 and capacity > 0:
            self.tray_type = tray_type
            self.footprint = footprint
            self.capacity = capacity
        else:
            raise ValueError("Make sure that you have entered the correct datatypes for the parameters.")

    def to_qt_table(self) -> List[str]:
        qt_table = []

        qt_table.append(str(self.tray_type))
        qt_table.append(str(self.capacity))
        qt_table.append(str(self.footprint))

        return qt_table


@dataclass(repr=True)
class PlantEntry:
    """
    Class to make a new Plant Entry (for in the database)
    Contains all data for a plant and its information
    """
    plant: Plant
    location: Location
    planting_time: datetime
    tray_type: Tray

    def __init__(self, plant: Plant, location: Location, planting_time: datetime, tray_type: Tray) -> None:
        pass
