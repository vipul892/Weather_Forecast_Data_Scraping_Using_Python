
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options() # config browser setting befor launching
    
    options.add_argument("--window-size=1920,1080")  # screen size

    driver = webdriver.Chrome(options=options)
    
    return driver