#AIO-Nookipedia
A simple, all-in-one python wrapper for the Nookipedia API

Nookipedia is a community-driven Animal Crossing wiki.
The main page of the Nookipedia wiki can be found [here](https://nookipedia.com/wiki/Main_Page).

##General Usage:
Every endpoint in the API is accessible through the `get` functions inside `NookClient` found in [client.py](src\aionookipedia\client.py)

For security in your own project, it is best if you use python-dotenv to load your api key, but you can pass the api key into `NookClient()` 
manually if you wish.

```python
import asyncio
from aionookipedia.client import NookClient 
from dotenv import load_dotenv
import os

#Example Usage:
        
async def main():
    load_dotenv()
    apiKey = os.getenv("API_KEY")
    async with NookClient(apiKey) as client:
        data = await client.getFish('pike')
        print(data.name)

asyncio.run(main())
```





