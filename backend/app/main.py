import os
import requests
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    return conn

# Get weather data from OpenWeatherMap
def get_weather_data():
    api_key = os.environ['OPENWEATHERMAP_API_KEY']
    url = f'http://api.openweathermap.org/data/2.5/weather?q=Budapest&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description']
    }

    return weather_data

# Route to fetch weather data and save it to the database
@app.route('/weather')
def weather():
    weather_data = get_weather_data()
    city = weather_data['city']
    temperature = weather_data['temperature']
    humidity = weather_data['humidity']
    description = weather_data['description']

    # Insert the weather data into the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO weather_logs (city, temperature, humidity, description)
        VALUES (%s, %s, %s, %s)
    """, (city, temperature, humidity, description))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)