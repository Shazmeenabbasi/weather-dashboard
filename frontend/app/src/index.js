import axios from 'axios';
import React, { useEffect, useState } from 'react';

function App() {
  const [weather, setWeather] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get(process.env.BACKEND_URL)
      .then(response => {
        setWeather(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching weather data:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Weather Dashboard</h1>
      {weather ? (
        <div>
          <h2>{weather.city}</h2>
          <p>Temperature: {weather.temperature}°C</p>
          <p>Humidity: {weather.humidity}%</p>
          <p>Weather: {weather.description}</p>
        </div>
      ) : (
        <p>No weather data available</p>
      )}
    </div>
  );
}

export default App;