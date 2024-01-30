import warnings
warnings.filterwarnings("ignore")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


def getTopTracks():
    # URL of Knock2's popular tracks on SoundCloud
    url = "https://soundcloud.com/knock2music/popular-tracks"

    # Set up the Selenium WebDriver
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)

    # Navigate to the page
    browser.get(url)

    # Wait for the dynamic content to load
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.soundTitle__title'))
        )
    except Exception as e:
        print("Error waiting for page elements to load:", e)
        browser.quit()
        return

    # Extract the track titles
    track_elements = browser.find_elements(By.CSS_SELECTOR, '.soundTitle__title')
    for track in track_elements:
        print(track.text)

    # Close the browser
    browser.quit()


def upcomingEvents():
    # URL of Knock2's upcoming events on personal webiste
    url = "https://www.knock2music.com/"

    #set up selenium driver
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)

    # Navigate to the page
    browser.get(url)

    # Wait for the dynamic content to load
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.MuiTypography-body1'))
        )
    except Exception as e:
        print("Error waiting for page elements to load:", e)
        browser.quit()
        return
    
     # Extract the track titles
    event_elements = browser.find_elements(By.CSS_SELECTOR, '.MuiTypography-body1')
    for events in event_elements:
        print(events.text)
    
    browser.quit

getTopTracks()
upcomingEvents()
