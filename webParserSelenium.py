from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import fake_useragent
import requests
import csvImport
import time
# Web parser for top-250 films on IMDb
link = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

# Chrome webdriver settings
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")
# Change User-Agent
user = fake_useragent.UserAgent().random
options.add_argument(f"user-agent={user}")

driver = webdriver.Chrome(options=options)

driver.get(link)

print("Spctipt Successfully Started!...")
time.sleep(2)

fullBlock = driver.find_element(By.CSS_SELECTOR, "ul.ipc-metadata-list--dividers-between")

filmList = fullBlock.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")

i = 0

for film in filmList:
    i += 1
    # Url
    filmUrl = film.find_element(By.CSS_SELECTOR, "a.ipc-title-link-wrapper")
    filmHref = filmUrl.get_attribute('href')
    # Name
    filmName = film.find_element(By.CSS_SELECTOR, "h3.ipc-title__text").text
    filmNameFinal = filmName[4:]
    # Release & Runtime
    filmInfo = film.find_element(By.CSS_SELECTOR, "div.sc-dc48a950-7")
    infoItems = filmInfo.find_elements(By.CSS_SELECTOR, "span.sc-dc48a950-8")
    # Release
    filmRelease = infoItems[0].text
    # Runtime
    filmRuntime = infoItems[1].text

    print(f"{i}. {filmNameFinal} | {filmHref} | {filmRelease} | {filmRuntime}")

    