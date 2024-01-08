
import requests
import time

API_KEY = "8cbf89c97d4244ec995211648240701"
BASE_URL = "https://api.weatherapi.com/v1/current.json"
FCities = "cities.txt"


def get_weather(city):
    params = {"key": API_KEY, "q": city}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()  #json is to parse the data as dictionary
        return data
    else:
        # failed
        print("Error fetching weather data.")
        return None


#display details
def dataW(weather_data):
    print(weather_data)
def display_weather(weather_data):
    if weather_data:
        # not empty
        print(f"Weather in {weather_data['location']['name']}, {weather_data['location']['region']}")
        print(f"Temperature: {weather_data['current']['temp_c']}°C")
        print(f"Condition: {weather_data['current']['condition']['text']}")
    else:
        print("Weather data not available.")


def show_cities():
    try:
        with open(FCities, "r") as file:
            return file.read().splitlines()  # splited into list of lines
    except FileNotFoundError:
        return None


def update_cities(cities):
    with open(FCities, "w") as file:
        for city in cities:
            file.write(f"{city}\n")


#main function
def main():
    while True:
        print("\nWeather Checking Application")
        print("1. Check weather by city name")
        print("2. CRUD operations on favorite list of cities")
        print("3. Auto-refresh every 15 seconds")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city_name = input("Enter the city name: ")
            weather_data = get_weather(city_name)
            # dataW(weather_data)
            display_weather(weather_data)
        elif choice == "2":
            favorite_cities = show_cities()
            print("Favorite Cities:", favorite_cities)
            print("1. Add city to favorites")
            print("2. Remove city from favorites")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                new_city = input("Enter the city to add to favorites: ")
                favorite_cities.append(new_city)
                update_cities(favorite_cities)
            elif sub_choice == "2":
                remove_city = input("Enter the city to remove from favorites: ")
                if remove_city in favorite_cities:
                    favorite_cities.remove(remove_city)
                    update_cities(favorite_cities)
                else:
                    print("City not found in favorites.")
        elif choice == "3":
            print("Auto-refresh every 15 seconds. Press Ctrl+C to stop.")
            while True:
                city_name = input("Enter the city name: ")
                weather_data = get_weather(city_name)
                display_weather(weather_data)
                time.sleep(15)
        elif choice == "0":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
