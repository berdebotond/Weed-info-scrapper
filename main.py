import json
import logging
import os

from modules.config.ini_config import config
from modules.scrapper.scrapper import Scrapper
from modules.strain_info.strain_info import StrainInfo

if config.get("APP","DEBUG"):
    logger = logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

def readJson(path: str = None) -> list:

    if path == None:
        path = os.path.abspath(os.getcwd()) + "/strain_name.json"

    with open(path) as f:
       strain_data = json.load(f)

    return strain_data["names"]

if __name__ == '__main__':

    names = readJson()

    scrapper = Scrapper(url=config.get("SCRAPPER","BASE_URL"), name="", load=False)

    for name in names:

        scrapper.update(url=config.get("SCRAPPER","BASE_URL"), name=name)
        try:
            scrapper.login_click()

        except Exception as ex:
            logging.info(f"Missing login")
            logging.debug(f"Error: {ex} ")

        try:
            strain_info = StrainInfo(scrapper.scrap_weed_info())

        except Exception as ex:

            logging.error(f"{name} not found")
            logging.debug(f"Error: {ex} ")
            continue

        strain_info.save_qr_code()
        del strain_info


