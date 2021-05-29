"""
Module used to gather Plant Data and plant types from the internet for my database.

Can be ignored for the final exercise
"""
from typing import List
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from requests import get


def write_to_file() -> None:
    """
    Get all plant names from site and write them to plants.txt
    """
    url = "https://www.batterijen.nl/vaste-planten-/complete-lijst--vaste-planten/pagina/1/aantal/1000000"

    res = get(url)

    soup = BeautifulSoup(res.text, 'html.parser')

    prod_desc: ResultSet = soup.find_all(class_="product-description")

    with open('C:\\Users\\tjalw\\Documents\\GitHub\\PyNursery\\src\\web_scraper\\plants.txt', 'w') as file:
        for prod in prod_desc:
            plant_name: str = prod.span.text
            if "'" in plant_name:
                # Only write if it has '' in the string because only then
                # we can decide what te latin family name is
                file.write(plant_name + '\n')


def get_unique_latin_names() -> List[str]:
    lines: List[str] = []
    with open('C:\\Users\\tjalw\\Documents\\GitHub\\PyNursery\\src\\web_scraper\\plants.txt', 'r+') as file:
        lines = file.readlines()

    latin_names: List[str] = []
    for plant in lines:
        latin_name = plant.split("'")[0]
        # name = plant.split("'")[1]
        latin_names.append(latin_name.strip())
        
    # Only get unique values
    latin_names = list(set(latin_names))
    # Append newline behind every name for writing to file
    latin_names = [x + '\n' for x in latin_names]
    with open('C:\\Users\\tjalw\\Documents\\GitHub\\PyNursery\\src\\web_scraper\\latin_names.txt', 'w') as file:
        file.writelines(latin_names)


if __name__ == '__main__':
    write_to_file()
    get_unique_latin_names()