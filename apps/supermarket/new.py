import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import re
import time
from twocaptcha import TwoCaptcha

urls = ['https://www.rewe.de/', 'https://www.lidl.de/', 'https://www.edeka.de/', 'https://www.kaufland.de/', 'https://www.aldi-sued.de/de/homepage.html', 
'https://www.aldi-nord.de/', 'https://www.netto-online.de/', 'https://www.penny.de/', 'https://www.meinreal.de/', 'https://www.norma-online.de/de/angebote/', 'https://www.tegut.com/',
'https://www.dm.de/', 'https://www.rossmann.de/de/','https://www.globus-baumarkt.de/', 'https://www.mueller.de/', 'https://www.fressnapf.de/', 'https://www.saturn.de/', 'https://www.mediamarkt.de/', 'https://www.otto.de/suche/Marken%20Media'] 

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept_language": "de-DE,de;q=0.9,es-ES;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5",
}

firefox_options = Options()
firefox_options.headless = True
driver = webdriver.Firefox(options = firefox_options, service=Service(executable_path=GeckoDriverManager().install()))

for website in urls:
    response = requests.get(website)
    data = BeautifulSoup(response.text, "html.parser")
#     elements = data.find_all(["a", "span", "button"], text=re.compile(r"Erlauben", re.IGNORECASE))
    elements = driver.find_elements(By.XPATH, "//button[contains(text(), 'Erlauben')]|//button[contains(text(), 'Zustimmen')]|//button[contains(text(), 'Akzeptieren')]|//button[contains(text(), 'Annehmem')]|//button[contains(text(), 'Zulassen')]|//button[contains(text(), 'zulassen')]|//button[contains(text(), 'akzeptieren')]|//button[contains(text(), 'bestätigen')]|//button[contains(text(), 'zustimmen')]|//button[contains(text(), 'ablehnen')]|//button[contains(text(), 'OK')]|//button[contains(text(), 'Mehr Optionen')]|//div[contains(text(), 'Erlauben')]")
    a = ActionChains(driver)
    # html_content.append(response.content)
    # if len(elements) > 0:
    #     for element in elements:
    #         print(element)
    print(len(elements))
