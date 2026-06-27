# 🌦️ Weather Forecast Web Scraping using Selenium

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/Selenium-Web%20Automation-43B02A?logo=selenium" />
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas" />
  <img src="https://img.shields.io/badge/CSV-Data%20Storage-orange" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen" />
</p>

---

# 📖 Project Overview

The **Weather Forecast Web Scraping** project is a Python automation application that extracts weather forecast information from a weather website using **Selenium WebDriver**.

The scraped weather data is processed and stored in both:

- 📄 **CSV File**
- 🗄️ **MySQL Database**

This project demonstrates browser automation, web scraping, file handling, database connectivity, and structured data storage.

---

# 🎯 Objective

The objective of this project is to automate the process of collecting weather information from a website and storing it in multiple formats for future analysis and reporting.

---

# ✨ Features

- 🌐 Automated Browser Control using Selenium
- 🔍 Weather Data Scraping
- 📄 CSV File Storage
- 🗄️ MySQL Database Storage
- ⚡ Fast Data Extraction
- ❌ Exception Handling
- 📊 Structured Data Management
- 🐍 Beginner-Friendly Python Project

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| 🐍 Python | Programming Language |
| 🤖 Selenium | Browser Automation |
| 🗄️ MySQL | Database Storage |
| 🐼 Pandas | Data Processing |
| 📄 CSV | File Storage |
| 🔗 MySQL Connector | Database Connectivity |
| 💻 VS Code | IDE |
| 🗂️ Git & GitHub | Version Control |

---
---

# ⚙️ Workflow

```text
               Start
                  │
                  ▼
        Launch Chrome Browser
                  │
                  ▼
         Open Weather Website
                  │
                  ▼
          Search for City Name
                  │
                  ▼
        Extract Weather Information
                  │
          ┌───────┴────────┐
          ▼                ▼
 Store Data in CSV   Store Data in MySQL
          │                │
          └───────┬────────┘
                  ▼
          Close Browser
                  │
                  ▼
                 End
```

---

# 📥 Input

The user enters a city name.

Example:

```text
Pune
```

---

# 📤 Extracted Weather Information

The application extracts the following information:

- 🌍 City Name
- 🌡️ Temperature
- ☁️ Weather Condition
- 💧 Humidity
- 💨 Wind Speed
- 📈 Pressure
- 📅 Date & Time (Optional)

---

# 📄 CSV Output

The extracted data is saved in:

```text
data/weather_data.csv
```

Example:

| City | Temperature | Condition | Humidity | Wind Speed | Pressure |
|------|-------------|-----------|----------|------------|----------|
| Pune | 30°C | Cloudy | 72% | 15 km/h | 1008 hPa |
| Mumbai | 29°C | Rainy | 81% | 18 km/h | 1005 hPa |
| Delhi | 39°C | Sunny | 35% | 12 km/h | 1002 hPa |

---

# 🗄️ MySQL Database

## Database

```sql
weather_db
```

---

## Table

```sql
weather_data
```

---

## Table Structure

| Column | Data Type |
|----------|------------|
| id | INT (Primary Key) |
| city | VARCHAR(100) |
| temperature | VARCHAR(20) |
| condition | VARCHAR(100) |
| humidity | VARCHAR(20) |
| wind_speed | VARCHAR(20) |
| pressure | VARCHAR(20) |
| scraped_at | DATETIME |

---

# 🖥️ Sample SQL Table

| id | city | temperature | condition | humidity | wind_speed | pressure |
|----|------|-------------|-----------|----------|------------|----------|
| 1 | Pune | 30°C | Cloudy | 72% | 15 km/h | 1008 hPa |
| 2 | Mumbai | 29°C | Rainy | 81% | 18 km/h | 1005 hPa |

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/Weather_Forecast_WebScraping.git
```

---

## Navigate to Project Folder

```bash
cd Weather_Forecast_WebScraping
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📄 requirements.txt

```text
selenium
pandas
mysql-connector-python
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 📚 Python Concepts Used

- Variables
- Functions
- Loops
- Selenium WebDriver
- File Handling
- CSV Operations
- MySQL Database Connectivity
- Exception Handling
- Data Processing using Pandas

---

---

# 🚀 Future Enhancements

- 🌍 Scrape Weather for Multiple Cities
- ⏰ Automatic Daily Weather Updates
- 📊 Interactive Dashboard using Streamlit
- 📈 Weather Trend Analysis
- 📧 Email Notifications
- ☁️ Cloud Deployment
- 📱 REST API Integration

---

# 📈 Learning Outcomes

By completing this project, you will gain practical experience in:

- Selenium Web Automation
- Web Scraping Techniques
- HTML Element Inspection
- CSV File Handling
- MySQL Database Operations
- Python Exception Handling
- Data Storage and Management
- Git & GitHub Version Control

---


# 👨‍💻 Author

**Vipul Alsundkar**
💼 Data Analytics & Data Science Enthusiast
---

<div align="center">

### ⭐ If you found this project helpful, please give it a Star! ⭐

**Happy Coding! 🚀**

</div>
