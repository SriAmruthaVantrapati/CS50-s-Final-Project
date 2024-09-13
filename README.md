# Weather Forecast
#### Video Demo:  <https://youtu.be/YPo_g1C8Fvk?si=SpxfwpaalY-57aat>
#### Description:
The Weather Forecast CLI Tool is a command-line application that retrieves and displays the current weather forecast for a specified location. It interacts with the OpenWeatherMap API to fetch real-time weather data and presents it in a user-friendly format. Users can specify the location and temperature unit (Celsius, Fahrenheit, or Kelvin), and the tool will display the temperature, weather description, and humidity.

This tool is useful for anyone who wants to quickly check the weather for any location directly from the command line.

## Features
- Fetches real-time weather data for any specified location.
- Displays temperature, weather description, and humidity.
- Supports different temperature units: Celsius, Fahrenheit, and Kelvin.
- Handles errors for invalid locations and network issues.

## Requirements
- Python 3.x
- `requests` library
- `pytest` library for testing

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/SriAmruthaVantrapati/weather-forecast-cli.git
    cd weather-forecast-cli
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Obtain an API key from OpenWeatherMap**:
    - An API key at [OpenWeatherMap]

## Usage
Run the CLI tool to get the weather forecast for a location:

```bash
python project.py "City Name" --unit metric
