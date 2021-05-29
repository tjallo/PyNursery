import re


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
