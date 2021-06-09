import re
import json


def is_valid_name(name: str) -> bool:
    """
    Checks wether a string is a valid name
    String is valid when it uses alphanumeric characters and spaces

    Args:
        name (str): name to be checked
    Returns:
        valid (bool): validity of string
    """
    pattern = '^[a-zA-Z0-9 ]*$'
    return re.match(pattern, name)


def get_db_path() -> str:
    """
    Returns path of database as set by user in the config
    """
    with open('./config/settings.json', 'r') as file:
        config = json.load(file)
        return config['DB-PATH']


def set_db_path(cwd: str) -> None:
    """
    Sets db_path in config automatically

    Args:
        cwd (str): root directory of PyNursery repo
    """

    act_path = f"{cwd}\\db"

    try:
        with open('./config/settings.json', 'r') as file:
            config = json.load(file)

    except:
        config = {'DB-PATH': 'none'}

    config['DB-PATH'] = act_path
    with open('./config/settings.json', 'w') as file:
        json.dump(config, file)
