# Django Weather Forecast Website

This Django web application allows users to enter a **location** or **zipcode** and get:
- The **current weather** at that location.
- A **5-day forecast**, with each day's weather and icons.

Weather data is retrieved from the [WeatherAPI](https://www.weatherapi.com/) service.

---

## Setup Instructions

### 1. Clone the Project from GitHub

```bash
git clone https://github.com/damiraskme/weather-site.git
touch .env
cd weatherSite
```
### 2. Add the following line to .env

```.env
WEATHER_API_KEY=your_actual_api_key_here
```

### 3. Install requirments

```bash
pip install -r requirements.txt
```

### 4. Django Setup

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 5. Open local running server

http://127.0.0.1:8000/weather