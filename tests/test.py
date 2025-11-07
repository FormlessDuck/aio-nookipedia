import asyncio
from aionookipedia.client import NookClient 
import time

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
    async with NookClient() as client:
        data = await client.getFish('pike')
        print(data.name)

asyncio.run(main())