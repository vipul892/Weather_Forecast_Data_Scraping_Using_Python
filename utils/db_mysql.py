import mysql.connector
from utils.logger import log


class MySQLDB:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Vipul@321",
            database="weather_db"
        )
        self.cursor = self.conn.cursor()

    def insert_bulk(self, data_list):
        query = """
        INSERT INTO weather_data (
            city, datetime, current_temp, high_temp, low_temp,
            weather_condition, feels_like, humidity,
            wind_degree, wind_direction, wind_speed,
            gust_speed, cloud_cover, visibility,
            pressure, uv_index
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = [
            (
                d.get("City name"),
                d.get("Current Datetime"),
                d.get("Current Temp"),
                d.get("Today High Temp"),
                d.get("Today Low Temp"),
                d.get("Weather Condition"),
                d.get("Feels Like"),
                d.get("Humidity"),
                d.get("Wind Degree") or 0,            
                d.get("Wind Direction") or "Unknown", 
                d.get("Wind Speed"),
                d.get("Gust Speed"),
                d.get("Cloud Cover"),
                d.get("Visibility"),
                d.get("Pressure"),
                d.get("UV Index")
            )
            for d in data_list
        ]

        try:
            self.cursor.executemany(query, values)
            self.conn.commit()
            log("✅ Data inserted into MySQL successfully")
        except Exception as e:
            log(f"❌ MySQL Insert Error: {e}")

    def close(self):
        self.cursor.close()
        self.conn.close()