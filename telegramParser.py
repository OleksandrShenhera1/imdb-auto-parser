from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import fake_useragent

def parser():
    # Web parser for top-250 films on IMDb
    link = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

    # Chrome webdriver settings
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--window-size=1920,1080')
    # Change User-Agent
    user = fake_useragent.UserAgent().random
    options.add_argument(f"user-agent={user}")

    driver = webdriver.Chrome(options=options)

    driver.get(link)
    

    fullBlock = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "ul.ipc-metadata-list--dividers-between"))
) 

    print("Spctipt Successfully Started!...")

    WebDriverWait(driver, 10).until(
    lambda d: fullBlock.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
)
    filmList = fullBlock.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
    i = 0

    films = []

    for film in filmList:
        i += 1
        # Name
        filmName = film.find_element(By.CSS_SELECTOR, "h3.ipc-title__text").text
        filmNameFinal = filmName.split(". ", 1)[1] if ". " in filmName else filmName
        
        # Rating
        filmRating = film.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--rating").text

        # Url
        filmUrl = film.find_element(By.CSS_SELECTOR, "a.ipc-title-link-wrapper")
        filmHref = filmUrl.get_attribute('href')
        # Printing info to terminal
        print(f"{i}. {filmNameFinal} | {filmRating} | {filmHref}")
        
        # Saving to dictionary
        filmDict = {
            "name": filmNameFinal,
            "rating": filmRating,
            "url": filmHref
        }
        films.append(filmDict)
    driver.quit()
    return films
