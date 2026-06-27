from scraper.driver_setup import get_driver
from scraper.current_weather_scraper import CurrentWeatherScraper
from config.settings import BASE_URL, CITIES, OUTPUT_FILE
from utils.logger import log
from utils.db_mysql import MySQLDB


def run():
    driver = get_driver()
    

    try:
        scraper = CurrentWeatherScraper(driver)
        db=MySQLDB()

        all_data = []

        for city in CITIES:
            url = BASE_URL.format(city)

            data = scraper.scrape_city(city, url)

            if data:
                all_data.append(data)

        log(f"Collected Data: {all_data}")

        scraper.save_data(all_data, OUTPUT_FILE)

        if all_data:
            db.insert_bulk(all_data)


    finally:
        driver.quit()
        try:
            db.close()
        except:
            pass    


if __name__ == "__main__":
    run()