# Weather CLI Application

A command-line application that interacts with the OpenWeather API to manage weather details of cities.

## Features

1. **Search for Weather Details of a City**: Enter the name of a city and display its current weather details using the OpenWeather API.
2. **Add a City to Favourites**: Add cities to your favourites list (maximum of 3 cities).
3. **List Favourite Cities**: Display all favourite cities along with their current weather details.
4. **Update Favourite Cities**: Remove a city from favourites and optionally add a new one, maintaining the limit of 3 cities.

## Requirements

- Python 3.7 or higher
- An OpenWeather API key

## Installation

### Option 1: Automated Setup (Recommended)

1. **Run the setup script**:
   ```bash
   ./setup.sh
   ```
   
   This will:
   - Create a virtual environment
   - Install all dependencies
   - Provide instructions for running the app

### Option 2: Manual Setup

1. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Get Your OpenWeather API Key

- Sign up for a free account at [OpenWeather](https://openweathermap.org/api)
- Navigate to your API keys section
- Copy your API key

## Usage

1. **Activate the virtual environment** (if not already activated):
   ```bash
   source venv/bin/activate
   ```

2. **Run the application**:
   ```bash
   python weather_app.py
   ```

3. **Enter your OpenWeather API key** when prompted

4. **When finished, deactivate the virtual environment**:
   ```bash
   deactivate
   ```

### Main Menu Options

```
1. Search for Weather Details of a City
   - Enter a city name to view its current weather

2. Add a City to Favourites
   - Add a city to your favourites list (max 3)
   - The city will be verified before adding

3. List Favourite Cities
   - View all your favourite cities
   - Display current weather for each city

4. Update Favourite Cities
   - Remove a city from favourites
   - Optionally add a new city

5. Exit
   - Close the application
```

## Weather Information Displayed

For each city, the application displays:
- 🌍 City name and country
- 🌡️ Temperature (Celsius) and "feels like" temperature
- ☁️ Weather condition (e.g., clear sky, light rain)
- 💧 Humidity percentage
- 💨 Wind speed (meters per second)

## Example Usage

```
==================================================
WEATHER APP SETUP
==================================================
Please enter your OpenWeather API key: your_api_key_here

🌤️ 🌤️ 🌤️ 🌤️ 🌤️ 🌤️ 🌤️ 🌤️ 🌤️ 🌤️ 
Welcome to the Weather CLI Application!
🌤️ 🌤️ 🌤️ 🌤️ 🌤️ 🌤️ 🌤️ 🌤️ 🌤️ 🌤️ 

==================================================
🌤️  WEATHER APP - MAIN MENU
==================================================
1. Search for Weather Details of a City
2. Add a City to Favourites
3. List Favourite Cities
4. Update Favourite Cities
5. Exit
==================================================

Enter your choice (1-5): 1
Enter city name: London

==================================================
🌍 Weather in London, GB
==================================================
🌡️  Temperature: 12.5°C (Feels like: 11.2°C)
☁️  Condition: Broken clouds
💧 Humidity: 76%
💨 Wind Speed: 4.5 m/s
==================================================
```

## Error Handling

The application handles some error scenarios:
- Invalid API key
- City not found
- Network connection issues
- Invalid user inputs
- API rate limiting

## Code Structure

```
weather_app.py
├── WeatherApp class
│   ├── __init__(): Initialize app with API key
│   ├── get_weather(): Fetch weather data from API
│   ├── display_weather(): Format and display weather info
│   ├── search_city_weather(): Search weather for a city
│   ├── add_to_favourites(): Add city to favourites
│   ├── list_favourites(): List all favourite cities
│   ├── update_favourites(): Remove/update favourites
│   ├── display_menu(): Show main menu
│   └── run(): Main application loop
└── main(): Entry point
```

## Notes

- Favourite cities are stored in memory only and will be lost when the application closes
- The application uses the free tier of OpenWeather API
- Temperature is displayed in Celsius (metric units)
- Maximum of 3 favourite cities can be stored at a time