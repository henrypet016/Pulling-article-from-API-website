from pyodide.http import pyfetch
import asyncio
        
async def fetch_data_and_write():
    response = await pyfetch(url="https://api.elifesciences.org/articles/84711", method="GET")
    json_response = await response.json()  # Parse the JSON response
    title = json_response.get('title', 'Title not found')
    output = f"{title}"
        
    pyscript.write('titleFinal',output)
        
        # To run the coroutine, you need to create an asyncio event loop
    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(fetch_data_and_write())