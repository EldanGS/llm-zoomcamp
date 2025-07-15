# weather_client.py
import asyncio
from fastmcp import Client
import json

async def main():
    """
    An asynchronous client to connect to the weather server,
    list its available tools, and print them in a readable format.
    """
    # The Client will start the server from weather_server.py as a subprocess.
    # This is the recommended way for standalone scripts.
    async with Client("weather_server.py") as mcp_client:
        print("Successfully connected to the weather server.")
        
        # The client exposes the server's methods. The JSON-RPC method 'tools/list'
        # is accessible via `mcp_client.tools.list()`.
        available_tools = await mcp_client.list_tools()
        # available_tools = await mcp_client.tools.list()
        
        print("\nListing available tools from the server:")
        # Use json.dumps for pretty-printing the JSON response
        print("available_tools: ", available_tools)
        # print(json.dumps(available_tools, indent=2))

        # --- Calling specific tools on the server ---

        # 1. Get the weather for a known city (Berlin)
        print("\nRequesting weather for Berlin...")
        # berlin_weather = await mcp_client.tools.get_weather(city="Berlin")
        berlin_weather = await mcp_client.call_tool("get_weather", arguments={"city": "Berlin"})
        print(f"Server response for Berlin: {berlin_weather}")

        # 2. Set the weather for a new city (Paris)
        print("\nSetting weather for Paris to 25 degrees...")
        # set_status = await mcp_client.tools.set_weather(city="Paris", temp=25.0)
        set_status = await mcp_client.call_tool("set_weather", arguments={"city": "Paris", "temp": 25.0})
        print(f"Server response for setting Paris: {set_status}")

        # 3. Get the newly set weather for Paris to confirm the change
        print("\nRequesting weather for Paris again...")
        # paris_weather = await mcp_client.tools.get_weather(city="Paris")
        paris_weather = await mcp_client.call_tool("get_weather", arguments={"city": "Paris"})
        print(f"Server response for Paris: {paris_weather}")

if __name__ == "__main__":
    print("Starting weather client...")
    # asyncio.run() is the standard way to execute an async main function.
    asyncio.run(main())