import asyncio
from aionookipedia.client import NookClient 
from dotenv import load_dotenv
import os

#Emaxple Usage:
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
    async with NookClient(apiKey) as client:
        data = await client.getFish('pike')
        print(data.name)

asyncio.run(main())