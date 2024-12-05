CREATE TABLE IF NOT EXISTS weather_logs (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    temperature FLOAT,
    humidity INT,
    description VARCHAR(255),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);