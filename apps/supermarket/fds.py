import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException, WebDriverException
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


urls = ['https://www.rewe.de/marktseite/hamburg/241061/rewe-markt-schoeneberger-str-31-35?ecid=seo_localseo_241061_g_nn_nn_nn_nn_nn', 'https://www.lidl.de/', 'https://www.edeka.de/', 'https://filiale.kaufland.de/?cid=F3183B02C1200K01000W01030000D1000E1000F1000G1000H1000', 'https://www.aldi-sued.de/de/homepage.html', 
'https://www.aldi-nord.de/filialen-und-oeffnungszeiten.html/l/hamburg/sieker-landstrasse-29/3181069', 'https://www.netto-online.de/filialen/Hamburg/Grindelhof-23/7350/', 'https://www.penny.de/', 'https://www.meinreal.de/', 'https://www.norma-online.de/de/angebote/', 'https://www.tegut.com/',
'https://www.dm.de/', 'https://www.rossmann.de/de/','https://www.globus-baumarkt.de/', 'https://www.mueller.de/', 'https://www.fressnapf.de/', 'https://www.saturn.de/', 'https://www.mediamarkt.de/', 'https://www.otto.de/suche/Marken%20Media'] 

# https://github.com/PatrickLib/captcha_recognize
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept_language": "de-DE,de;q=0.9,es-ES;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5",
}

firefox_options = Options()
firefox_options.headless = True
driver = webdriver.Firefox(options = firefox_options, service=Service(executable_path=GeckoDriverManager().install()))

for website in urls:
#     response = requests.get(website)
#     data = BeautifulSoup(response.text, "html.parser")
    driver.get(website)
#     elements = data.find_all(["a", "span", "button"], text=re.compile(r"Erlauben", re.IGNORECASE))
# DETERMINE IF THERE ARE COOKIES BUTTON
    elements = driver.find_elements(By.XPATH, "//button[contains(text(), 'Erlauben')]|//button[contains(text(), 'Zustimmen')]|//button[contains(text(), 'Akzeptieren')]|//button[contains(text(), 'Annehmem')]|//button[contains(text(), 'Zulassen')]|//button[contains(text(), 'zulassen')]|//button[contains(text(), 'akzeptieren')]|//button[contains(text(), 'bestätigen')]|//button[contains(text(), 'zustimmen')]|//button[contains(text(), 'ablehnen')]|//button[contains(text(), 'OK')]|//button[contains(text(), 'Mehr Optionen')]|//div[contains(text(), 'Erlauben')]")
    a = ActionChains(driver)
    # html_content.append(response.content)
    # if len(elements) > 0:
    #     for element in elements:
    #         print(element)
    if len(elements) > 0:
        for element in elements:
                print(element.text)
                print(website)
                try:
                    a.move_to_element(element).click()
                    print(website)
                    print("The Cookies button was cliked")

                except StaleElementReferenceException:
                    pass

    time.sleep(2)
    angeboteButtons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Angebote')]|//a[contains(text(), 'Angebote')]|//a[contains(text(), 'Angebote')]|//span[contains(text(), 'Angebote')]" )
    counter = 0
    time.sleep(2)
    if len(angeboteButtons) > 0:
        for button in angeboteButtons:
            try:
                # HERE THE CODE COULD START CHRASHING
                if button.is_displayed() and button.is_enabled():
                    print(button.text)
                    a.move_to_element(button).click().perform()
                    print(driver.current_url)
                    driver.back()
            except (StaleElementReferenceException, WebDriverException):
                print("We are going to try to reload this website:", website)
                continue