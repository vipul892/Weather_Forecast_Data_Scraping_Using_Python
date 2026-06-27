from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import log
from utils.retry import retry
from utils.helper import extract_number, extract_direcation
from config.settings import WAIT_TIME

import pandas as pd
from datetime import datetime
import time
import os


class CurrentWeatherScraper:
   
   # initialization
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIME)

    def open_page(self, url):
        log(f"Opening URL: {url}")
        self.driver.get(url)
        time.sleep(2)

    # Simple scroll
    def scroll_page(self):
        for _ in range(1):
            self.driver.execute_script("window.scrollBy(0, 600);")
            time.sleep(1)

    # text fetcher
    @retry(max_attempts=3, delay=2)
    def get_text(self, xpath):
        try:
            return self.wait.until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            ).text
        except:
            log(f"Failed XPath: {xpath}")
            return None

    # Reusable extractor
    def safe_extract(self, xpath, is_number=True):
        text = self.get_text(xpath)
        if not text:
            return "N/A"

        return extract_number(text) if is_number else text

    def scrape_city(self, city, url):
        log(f"Scraping city: {city}")
        self.open_page(url)

        # Scroll for lazy loading
        self.scroll_page()

        data = {
            "City name": city,
            "Current Datetime": datetime.now()
        }

        try:
            #  Temperature
            data["Current Temp"] = self.safe_extract('(//span[contains(@class,"items-baseline")])[1]')
            data["Today High Temp"] = self.safe_extract('(//span[@class="text-[0.3em]"])[1]')
            data["Today Low Temp"] = self.safe_extract('(//span[@class="text-[0.3em]"])[2]')

            # Weather
            data["Weather Condition"] = self.safe_extract(
                '//span[contains(@class,"leading-[1.2]")]', is_number=False
            )

            data["Feels Like"] = self.safe_extract('(//p[contains(@class,"flex flex-wrap")])[1]')
            data["Chances of Rain"] = self.safe_extract('(//p[contains(@class,"flex flex-wrap")])[2]')
            data["Air Quality Index (AQI)"] = self.safe_extract('//a[contains(@aria-label,"AQI")]')
            data["Humidity"] = self.safe_extract('//p[contains(text(),"Humidity")]/following::span[1]')

            # Wind (single fetch better performance)
            data["Wind Degree"] = extract_number(
                self.get_text("(//p[@class='value flex flex-wrap items-baseline gap-[0_0.2em] text-[2.5rem] sm:text-[3rem] text-dark_title leading-[100%] pt-[0.2em]'])[2]")
            ) or "N/A"

            wind_direction = self.get_text("(//p[@class='value flex flex-wrap items-baseline gap-[0_0.2em] text-[2.5rem] sm:text-[3rem] text-dark_title leading-[100%] pt-[0.2em]'])[2]")
            data["Wind Direction"] = extract_direcation(wind_direction) or "N/A"

            # Other metrics
            data["Wind Speed"] = self.safe_extract('//p[contains(text(),"Wind Speed")]/preceding::span[2]')
            data["Gust Speed"] = self.safe_extract('//p[contains(text(),"Gust Speed")]/following::span[1]')
            data["Cloud Cover"] = self.safe_extract('//p[contains(text(),"Cloud Cover")]/following::span[1]')
            data["Visibility"] = self.safe_extract('//p[contains(text(),"Visibility")]/following::span[1]')
            data["Pressure"] = self.safe_extract('//p[contains(text(),"Pressure")]/following::span[1]')
            data["UV Index"] = self.safe_extract('//p[contains(text(),"UV")]/following::span[1]')

        except Exception as e:
            log(f"Error scraping {city}: {e}")

        return data

    def save_data(self, data_list, file_path):
        df = pd.DataFrame(data_list)

        if not os.path.exists(file_path):
            df.to_csv(file_path, index=False)
        else:
            df.to_csv(file_path, mode='a', header=False, index=False)

        log("All city data saved successfully!")