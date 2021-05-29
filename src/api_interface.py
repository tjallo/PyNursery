from dataclasses import dataclass
from typing import Type
from src.utils import is_valid_name


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
