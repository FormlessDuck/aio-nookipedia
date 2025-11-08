# AIO-Nookipedia
A simple, all-in-one python wrapper for the Nookipedia API with caching

Nookipedia is a community-driven Animal Crossing wiki.
The main page of the Nookipedia wiki can be found [here](https://nookipedia.com/wiki/Main_Page).

## Installation
The wrapper can be installed via pip using 
`pip install aio-nookipedia`

## General Usage:
Every endpoint in the API is accessible through the `get` functions inside `NookClient` found in [client.py](https://github.com/FormlessDuck/aio-nookipedia/blob/main/src/aionookipedia/client.py)
These functions each return an object or list of objects containing all the data stored in the API.

Example Usage:
```python
import asyncio
from aionookipedia.client import NookClient 
        
async def main():
    async with NookClient("YOUR_API_KEY") as client:
        data = await client.getFish('pike')
        print(data.name) # will return "Pike"

asyncio.run(main())
```

Most attributes (eg. name, species, rarity, etc.) follow the same naming scheme as the API. The only exception to this is the "from" attribute in the `Availability` object that is stored in items. Since `from` is a keyword in Python, this can be accessed with .availability.location instead.

```python
async def getFurnitureByLocation(client, location: str):
    data = await getAllFurniture()
    furniture = []
    for x in data:
        if x.availability.location == location.title():
            furniture.append(x)
    return furniture # returns a list of all furniture that is available from the specified location
```

There is also a custom object called `FossilSet` that accesses an endpoint containing the `FossilGroup` objects with their respective fossils. I modified the objects stored here to contain an array of `Fossil` objects that are identical to the objects at the "Single New Horizons Fossil" endpoint.


For security in your own project, it is best if you use `python-dotenv` to load your api key, but you can pass the api key into `NookClient()` 
manually if you wish.


### Requirements
Python >= 3.13.7

[aiohttp-client-cache](https://aiohttp-client-cache.readthedocs.io/en/stable/user_guide.html)





