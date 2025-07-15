# weather_server.py
from fastmcp import FastMCP
import random 

mcp = FastMCP("Starting MCP server 'Demo 🚀'")

known_weather_data = {
    'berlin': 20.0
}

@mcp.tool
def get_weather(city: str) -> float:
    """
    Retrieves the temperature for a specified city.

    Args:
        city: The name of the city for which to retrieve weather data.

    Returns:
        The temperature associated with the city.
    """
    city = city.strip().lower()

    if city in known_weather_data:
        return known_weather_data[city]

    return round(random.uniform(-5, 35), 1)

@mcp.tool
def set_weather(city: str, temp: float) -> str:
    """
    Sets the temperature for a specified city.

    Args:
        city: The name of the city for which to set the weather data.
        temp: The temperature to associate with the city.

    Returns:
        A confirmation string 'OK' indicating successful update.
    """
    city = city.strip().lower()
    known_weather_data[city] = temp
    return 'OK'


if __name__ == "__main__":
    mcp.run()
