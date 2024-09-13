import pytest
from project import get_weather_data, parse_weather_data

def test_get_weather_data(monkeypatch):
    class MockResponse:
        @staticmethod
        def json():
            return {
                "name": "London",
                "main": {"temp": 280, "humidity": 75},
                "weather": [{"description": "clear sky"}]
            }

        @staticmethod
        def raise_for_status():
            pass

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    data = get_weather_data("London", "kelvin")
    assert data["name"] == "London"
    assert "main" in data
    assert "weather" in data

def test_parse_weather_data():
    raw_data = {
        "name": "London",
        "main": {"temp": 280, "humidity": 75},
        "weather": [{"description": "clear sky"}]
    }
    forecast = parse_weather_data(raw_data, "kelvin")
    assert forecast["location"] == "London"
    assert forecast["temperature"] == 280
    assert forecast["description"] == "clear sky"
    assert forecast["humidity"] == 75
