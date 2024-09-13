import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="Get the weather forecast for a specific location.")
    parser.add_argument("location", type=str, help="The location to get the weather forecast for.")
    parser.add_argument("--unit", type=str, choices=["metric", "imperial", "kelvin"], default="kelvin",
                        help="Unit of temperature (metric=Celsius, imperial=Fahrenheit, kelvin=Kelvin).")
    args = parser.parse_args()

    weather_data = get_weather_data(args.location, args.unit)
    if weather_data:
        forecast = parse_weather_data(weather_data, args.unit)
        display_forecast(forecast, args.unit)
    else:
        print(f"Could not retrieve weather data for {args.location}.")

def get_weather_data(location: str, unit: str) -> dict:
    api_key = "fff5bdea5330cc33f584f35e3e92f885"
    unit_param = "metric" if unit == "metric" else "imperial" if unit == "imperial" else "standard"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units={unit_param}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parse_weather_data(data: dict, unit: str) -> dict:
    forecast = {
        "location": data.get("name"),
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"]
    }
    return forecast

def display_forecast(forecast: dict, unit: str):
    unit_symbol = "°C" if unit == "metric" else "°F" if unit == "imperial" else "K"
    print(f"Weather Forecast for {forecast['location']}:")
    print(f"Temperature: {forecast['temperature']}{unit_symbol}")
    print(f"Description: {forecast['description'].capitalize()}")
    print(f"Humidity: {forecast['humidity']}%")

if __name__ == "__main__":
    main()
