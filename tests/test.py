import asyncio
from aionookipedia.client import NookClient 
from dotenv import load_dotenv
import os
import time

#Example Usage:
# async def getVillagersBySpecies(species: str):
#     data = await client.getAllVillagers()
#     villagers = []
#     for x in data:
#         if x.species == species.title():
#             villagers.append(x)
#         else:
#             continue
#     return villagers
        
async def main():
    load_dotenv()
    apiKey = os.getenv("API_KEY")
    start_time = time.time()
    async with NookClient(apiKey) as client:
        data = await client.getAllVillagers()
        for x in data:
            print(x.name)
        end_time = time.time()
        print(f"Execution Time: {end_time - start_time} seconds")
        
        

asyncio.run(main())