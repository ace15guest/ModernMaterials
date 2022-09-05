import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def OpenBrowser(driver, webaddress):
    """

    :param driver: Webdriver we will search the web with
    :param webaddress: Site We want to go to
    :return: None
    """
    driver.get(webaddress)
    return None

def country_picker(driver, countries):
    for country in countries:
        driver.find_element(By.XPATH,"[WDI_Ctry].[List].&[PAK]").click()


# Set path Selenium
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
s = Service(CHROMEDRIVER_PATH)
WINDOW_SIZE = "1920,1080"

#Create driver
driver = webdriver.Chrome(service=s)
world_data_url = "https://databank.worldbank.org/source/world-development-indicators"
OpenBrowser(driver, world_data_url)
time.sleep(3)
driver.find_element(By.ID,"chk[WDI_Ctry].[List].&[ARG]").click()
driver.find_element(By.XPATH, '//a[@href="#selectedDimension_WDI_Series"]').click()
time.sleep(3)
driver.find_element(By.ID,"chk[WDI_Series].[Topic].&[EG.CFT.ACCS.ZS]").click()


