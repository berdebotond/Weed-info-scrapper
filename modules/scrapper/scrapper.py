from selenium import webdriver
from selenium.webdriver.common.by import By

from modules.models.strain import WeedStrain


class Scrapper:
    """
    Login into leafy and scrap information about the given strains
    """

    def __init__(self, url: str, name: str, load: bool = True):
        """
        Search for a strain and init chromeDriver, send back error if page not found
        :param name: str = Strain anem
        :param url: str = Leafy url, name: str = Strain name
        :param load: bool = laod iniate page, if false you have to use .update func before login
        :return:None
        """
        self.strain = None
        self.name = name.replace(" ", "-").lower()
        self.url = url + self.name
        self.driver = webdriver.Chrome('chromedriver.exe')
        if load:
            self.driver.get(self.url)

    def update(self, name: str, url: str):
        """
        Update strain anme and url without open chromedriver again
        :param name: STrain name
        :param url: str = Leafy url, name: str = Strain name
        :return:
        """
        self.name = name.replace(" ", "-").lower()
        self.url = url + self.name
        self.strain = None
        self.driver.get(self.url)

    def login_click(self):
        """
        Step into leafy when it asks if we are old enough
        :return: None
        """
        button = self.driver.find_element(by=By.XPATH, value='//button[@class="button button--primary text-sm"]')
        button.click()
        self.driver.get(self.url)

    def scrap_weed_info(self) -> type(WeedStrain):
        """
        Scrap the description and effect of the weed strain
        :return: WeedStrain
        """
        # Searching for effects and description with xpath
        effects_drivers_obj = self.driver.find_elements(by=By.XPATH,
                                                        value='//p[@class="text-sm font-bold text-center mt-xs mb-none truncate w-full lowercase"]')
        description_obj = self.driver.find_elements(by=By.XPATH,
                                                    value='//div[@class="jsx-ab29da9b1f387cb mt-lg mb-xxl green-links"]')

        # Loop over the scraped data
        effects = []
        for effect in effects_drivers_obj:
            effects.append(effect.text)

        # Create strain obj
        self.strain = WeedStrain
        self.strain.name = self.name

        self.strain.good_effects = effects[0:3]
        self.strain.bad_effects = effects[3:6]
        self.strain.taste = effects[6:9]
        self.strain.description = description_obj[1].text

        return self.strain

    def __del__(self):
        self.driver.close()
