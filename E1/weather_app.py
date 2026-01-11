#!/usr/bin/env python3
"""
Comcast RDK program E1
"""

import requests
import sys
from typing import List, Dict, Optional


class WeatherApp:
    """    
    Attributes:
        api_key (str): OpenWeather API key
        base_url (str): Base URL for OpenWeather API
        favourite_cities (List[str]): List of favourite cities (max 3)
        max_favourites (int): Maximum number of favourite cities allowed
    """
    
    def __init__(self, api_key: str):
        """
        Initialize the Weather App.
        
        Args:
            api_key (str): OpenWeather API key
        """
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.favourite_cities: List[str] = []
        self.max_favourites = 3
    
    def get_weather(self, city: str) -> Optional[Dict]:
        """
        Fetch weather data for a given city from OpenWeather API.
        
        Args:
            city (str): Name of the city
            
        Returns:
            Optional[Dict]: Weather data dictionary if successful, None otherwise
        """
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # Use Celsius for temperature
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f"❌ City '{city}' not found. Please check the spelling and try again.")
                return None
            elif response.status_code == 401:
                print("❌ Invalid API key. Please check your API key and try again.")
                print("📝 Note: New API keys can take up to 2 hours to activate after creation.")
                print("   Verify your API key at: https://home.openweathermap.org/api_keys")
                return None
            else:
                print(f"❌ Error: Unable to fetch weather data (Status code: {response.status_code})")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error: {e}")
            return None
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            return None
    
    def display_weather(self, weather_data: Dict) -> None:
        """
        Display formatted weather information.
        
        Args:
            weather_data (Dict): Weather data from OpenWeather API
        """
        city = weather_data['name']
        country = weather_data['sys']['country']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        
        print("\n" + "="*50)
        print(f"🌍 Weather in {city}, {country}")
        print("="*50)
        print(f"🌡️  Temperature: {temp}°C (Feels like: {feels_like}°C)")
        print(f"☁️  Condition: {description.capitalize()}")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind_speed} m/s")
        print("="*50 + "\n")
    
    def search_city_weather(self) -> None:
        """Search and display weather details for a city."""
        city = input("Enter city name: ").strip()
        
        if not city:
            print("❌ City name cannot be empty.")
            return
        
        weather_data = self.get_weather(city)
        if weather_data:
            self.display_weather(weather_data)
    
    def add_to_favourites(self) -> None:
        """Add a city to the favourites list."""
        if len(self.favourite_cities) >= self.max_favourites:
            print(f"❌ You already have {self.max_favourites} favourite cities.")
            print("Please remove a city first using 'Update Favourite Cities' option.")
            return
        
        city = input("Enter city name to add to favourites: ").strip()
        
        if not city:
            print("❌ City name cannot be empty.")
            return
        
        # Verify the city exists by fetching its weather
        weather_data = self.get_weather(city)
        if weather_data:
            # Use the standardized city name from the API response
            standardized_city = weather_data['name']
            
            if standardized_city in self.favourite_cities:
                print(f"⚠️  '{standardized_city}' is already in your favourites.")
                return
            
            self.favourite_cities.append(standardized_city)
            print(f"✅ '{standardized_city}' has been added to your favourites!")
            print(f"You now have {len(self.favourite_cities)}/{self.max_favourites} favourite cities.")
    
    def list_favourites(self) -> None:
        """Display the list of favourite cities with their current weather."""
        if not self.favourite_cities:
            print("\n📋 You have no favourite cities yet.")
            print("Use option 2 to add cities to your favourites.\n")
            return
        
        print(f"\n⭐ Your Favourite Cities ({len(self.favourite_cities)}/{self.max_favourites}):")
        print("="*50)
        
        for i, city in enumerate(self.favourite_cities, 1):
            print(f"\n[{i}] {city}")
            weather_data = self.get_weather(city)
            if weather_data:
                self.display_weather(weather_data)
            else:
                print(f"⚠️  Unable to fetch weather data for {city}\n")
    
    def update_favourites(self) -> None:
        """Remove a city from favourites and optionally add a new one."""
        if not self.favourite_cities:
            print("\n📋 You have no favourite cities to update.")
            print("Use option 2 to add cities to your favourites.\n")
            return
        
        print("\n⭐ Current Favourite Cities:")
        for i, city in enumerate(self.favourite_cities, 1):
            print(f"{i}. {city}")
        
        try:
            choice = input("\nEnter the number of the city to remove (or 'c' to cancel): ").strip()
            
            if choice.lower() == 'c':
                print("❌ Update cancelled.")
                return
            
            index = int(choice) - 1
            
            if 0 <= index < len(self.favourite_cities):
                removed_city = self.favourite_cities.pop(index)
                print(f"✅ '{removed_city}' has been removed from favourites.")
                
                # Ask if user wants to add a new city
                if len(self.favourite_cities) < self.max_favourites:
                    add_new = input("\nWould you like to add a new city? (y/n): ").strip().lower()
                    if add_new == 'y':
                        self.add_to_favourites()
            else:
                print("❌ Invalid choice. Please enter a valid number.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
    
    def display_menu(self) -> None:
        """Display the main menu."""
        print("\n" + "="*50)
        print("🌤️  WEATHER APP - MAIN MENU")
        print("="*50)
        print("1. Search for Weather Details of a City")
        print("2. Add a City to Favourites")
        print("3. List Favourite Cities")
        print("4. Update Favourite Cities")
        print("5. Exit")
        print("="*50)
    
    def run(self) -> None:
        """Run the main application loop."""
        print("\n" + "🌤️ " * 10)
        print("Welcome to the Weather CLI Application!")
        print("🌤️ " * 10)
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                self.search_city_weather()
            elif choice == '2':
                self.add_to_favourites()
            elif choice == '3':
                self.list_favourites()
            elif choice == '4':
                self.update_favourites()
            elif choice == '5':
                print("\n👋 Thank you for using Weather App. Goodbye!")
                sys.exit(0)
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 5.")


def main():
    """Main entry point of the application."""
    print("\n" + "="*50)
    print("WEATHER APP SETUP")
    print("="*50)
    
    # Get API key from user
    api_key = input("Please enter your OpenWeather API key: ").strip()
    
    if not api_key:
        print("❌ API key is required to run the application.")
        print("📝 Get your free API key at: https://openweathermap.org/api")
        print("⏰ Note: New API keys can take up to 2 hours to activate.")
        sys.exit(1)
    
    # Initialize and run the app
    app = WeatherApp(api_key)
    app.run()


if __name__ == "__main__":
    main()
