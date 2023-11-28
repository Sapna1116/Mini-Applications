# #pip install --user bs4
# #pip install geopy

import requests
from bs4 import BeautifulSoup as bs
from geopy.geocoders import OpenCage

def get_temperature_from_google(place):
    search = f"weather in {place}"
    url = f"https://www.google.com/search?&q={search}"

    try:
        r = requests.get(url)
        r.raise_for_status()  # Check for HTTP errors
    except requests.RequestException as e:
        print(f"Error accessing Google search: {e}")
        return None

    s = bs(r.text, "html.parser")
    result_element = s.find("div", class_="BNeawe iBp4i AP7Wnd")

    if result_element is not None:
        result = result_element.text
        return result
    else:
        print(f"Could not find temperature information for {place}")
        return None

def check_city_existence(city, api_key):
    geolocator = OpenCage(api_key)
    try:
        location = geolocator.geocode(city)
        if location is not None:
            return True
        else:
            print(f"City '{city}' not found.")
            return False
    except Exception as e:
        print(f"Error checking city existence: {e}")
        return False

def read_api_key(file_path):
    try:
        with open(file_path, 'r') as file:
            api_key = file.read().strip()
        return api_key
    except FileNotFoundError:
        print("API key file not found.")
        return None

if __name__ == "__main__":
    api_key_file_path = "Weather Teller\API_Key_For_WeatherTeller.txt"  
    api_key = read_api_key(api_key_file_path)

    if api_key is None:
        print("Exiting due to missing API key.")
        exit()

    while True:
        place = input("Enter the city name to find out its current temperature status (enter 'q' to quit): ")

        if place.lower() == 'q':
            break

        if not place.isalpha():
            print("Invalid input. Please enter a valid city name or 'q' to quit.")
            continue

        # Check if the city exists
        if not check_city_existence(place, api_key):
            print("Invalid city name. Please enter a valid city name or 'q' to quit.")
            continue

        # Get temperature from Google search
        temperature = get_temperature_from_google(place)

        if temperature is not None:
            print(f"The current temperature in {place} is {temperature}")
