from dataclasses import dataclass
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
        if type(metadata) == dict:
            self.family_name = family_name.strip()
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


@dataclass(repr=True)
class PlantBatch:
    """
    Class to make a new PlantBatch (for in the database)
    The PlantBatch class is for actual Plants that are in your company
    Unlike Plant and PlantFamilies it isn't a database of plants that could be in your company
    Contains all data for a plant and its metadata
    """
    plant: Plant
    location: Location
    planting_time: datetime
    n_tray: int
    tray_type: Tray
    n_plants: int
    area_needed: float

    def __init__(self, plant: Plant, location: Location, tray_type: Tray, n_trays: int, planting_time: datetime = datetime.now()) -> None:
        """
        Constructor

        Args:
            plant (Plant): plant that has been planted
            location (Location): the location the plant is at
            tray_type (Tray): the type of tray that is used
            n_tray (int): The number of trays that have been placed at this location
            planting_time (datetime): the time at which the trays were first placed
        """
        if n_trays > 0 and (type(planting_time) == datetime):
            self.plant = plant
            self.location = location
            self.tray_type = tray_type
            self.n_tray = n_trays
            self.planting_time = planting_time
            self.n_plants = self.tray_type.capacity * n_trays
            self.area_needed = self.tray_type.footprint * n_trays

        else:
            raise ValueError("Please enter valid arguments for the parameters")

    def get_area(self) -> float:
        """
        Returns the area (in m^2) that this batch of plants takes up
        """
        return self.area_needed

    def get_plant_count(self) -> int:
        """
        Returns the amount of plants that are in this batch
        """
        return self.n_plants

    def get_age(self) -> int:
        """
        Returns age (in days) of the batch
        """
        return (datetime.now() - self.planting_time).days

    def get_plant_date(self) -> str:
        """
        Returns formatted (dd-mm-yyyy) string of the planting date of the batch
        """
        day: int = self.planting_time.day
        month: int = self.planting_time.month
        year: int = self.planting_time.year

        return f"{day}-{month}-{year}"

    def get_epoch(self) -> int:
        """
        Returns unix epoch (in seconds) of the timestamp
        """
        return self.planting_time.second
