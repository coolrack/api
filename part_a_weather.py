"""
Part A: Weather Information Program
Student: devin l.
API Documentation: https://github.com/chubin/wttr.in

This program uses the wttr.in API to fetch and display current weather
information for any city or location entered by the user.
"""

import requests
import json


def get_weather_emoji(weather_description):
    """
    Returns an appropriate emoji based on the weather description.
    This function matches keywords in the weather description to emojis.
    """
    weather_lower = weather_description.lower()
    
    # Check for different weather conditions and return matching emoji
    if 'sunny' in weather_lower or 'clear' in weather_lower:
        return '☀️'
    elif 'cloud' in weather_lower and 'partly' in weather_lower:
        return '⛅'
    elif 'cloud' in weather_lower or 'overcast' in weather_lower:
        return '☁️'
    elif 'rain' in weather_lower or 'drizzle' in weather_lower:
        return '🌧️'
    elif 'snow' in weather_lower:
        return '🌨️'
    elif 'storm' in weather_lower or 'thunder' in weather_lower:
        return '⛈️'
    elif 'fog' in weather_lower or 'mist' in weather_lower:
        return '🌫️'
    elif 'wind' in weather_lower:
        return '💨'
    else:
        return '🌤️'


def get_weather(location):
    """
    Makes an API request to wttr.in and retrieves weather data.
    Returns the JSON response or None if there's an error.
    """
    # Construct the API URL with JSON format parameter
    api_url = f"https://wttr.in/{location}?format=j1"
    
    try:
        # Make the GET request to the API
        response = requests.get(api_url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch weather data (Status code: {response.status_code})")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Connection problem - {e}")
        return None


def display_weather(weather_data, location):
    """
    Formats and displays the weather information in a user-friendly way.
    Extracts temperature, conditions, and displays emoji.
    """
    # Extract current weather conditions from the API response
    current_condition = weather_data['current_condition'][0]
    
    # Get temperature in Celsius (API provides this)
    temp_celsius = current_condition['temp_C']
    
    # Get temperature in Fahrenheit (API provides this)
    temp_fahrenheit = current_condition['temp_F']
    
    # Get weather description (e.g., "Partly cloudy", "Clear")
    weather_description = current_condition['weatherDesc'][0]['value']
    
    # Get the appropriate emoji for the weather
    weather_emoji = get_weather_emoji(weather_description)
    
    # Display the weather information in a formatted way
    print("\n" + "="*50)
    print(f"🌍 Weather for: {location.title()}")
    print("="*50)
    print(f"\n{weather_emoji}  Weather Conditions: {weather_description}")
    print(f"🌡️  Temperature: {temp_celsius}°C / {temp_fahrenheit}°F")
    print(f"💧 Humidity: {current_condition['humidity']}%")
    print(f"💨 Wind Speed: {current_condition['windspeedKmph']} km/h")
    print(f"👁️  Visibility: {current_condition['visibility']} km")
    print("="*50 + "\n")


def main():
    """
    Main function that runs the weather program.
    Gets user input and displays weather information.
    """
    print("="*50)
    print("     Welcome to the Weather Information App!")
    print("="*50)
    
    # Get location input from the user
    location = input("\nEnter a city or location: ").strip()
    
    # Validate that the user entered something
    if not location:
        print("Error: Please enter a valid location.")
        return
    
    print(f"\nFetching weather data for '{location}'...")
    
    # Retrieve weather data from the API
    weather_data = get_weather(location)
    
    # If data was successfully retrieved, display it
    if weather_data:
        display_weather(weather_data, location)
    else:
        print("Unable to retrieve weather information. Please try again.")


# Entry point of the program
if __name__ == "__main__":
    main()
