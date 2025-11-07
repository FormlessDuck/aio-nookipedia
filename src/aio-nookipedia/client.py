from aiohttp_client_cache.session import CachedSession
import os
from resources import Villager
from resources import Recipe
from resources import Event
from dotenv import load_dotenv
from resources.museum import (
    Fish,
    Bug,
    SeaCreature,
    Artwork,
    Fossil,
    FossilGroup,
    FossilSet
)
from resources.items import (
    Clothing, 
    Furniture,
    InteriorItem,
    Tool,
    Photo,
    MiscItem,
    Gyroid
)

apiVersion = "1.7.0"
load_dotenv()

class NookClient:

    def __init__(self, baseUrl = "https://api.nookipedia.com"):
        self.baseUrl = baseUrl
        self.session = CachedSession(expire_after=21600) #Cache expires after 6 hours
        self.apiKey = os.getenv("API_KEY")

    async def __aenter__(self):
        return self
    
    async def __aexit__(self, *args):
       await self.close()

    async def close(self):
        await self.session.close()

    async def fetchJson(self, url: str):
        header = {"X-API-KEY": self.apiKey, "Accept-Version": apiVersion}  
        response = await self.session.get(url, headers=header)
        return await response.json()
            
    async def getVillager(self, name: str):
        data = await self.fetchJson(f"{self.baseUrl}/villagers?name={name}&nhdetails=true".lower())
        villager = Villager(data[0])
        return villager
    
    async def getAllVillagers(self):
        villagers_raw = await self.fetchJson(f"{self.baseUrl}/villagers?nhdetails=true".lower())
        villagers = []
        for x in villagers_raw:
            villagers.append(Villager(x))
        return villagers
    
    async def getFish(self, name: str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/fish/{name}".lower())
        fish = Fish(data)
        return fish
    
    async def getAllFish(self):
        fish_raw = await self.fetchJson(f"{self.baseUrl}/nh/fish".lower())
        fish = []
        for x in fish_raw:
            fish.append(Fish(x))
        return fish

    async def getBug(self, name: str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/bugs/{name}".lower())
        bug = Bug(data)
        return bug
    
    async def getAllBugs(self):
        bugs_raw = await self.fetchJson(f"{self.baseUrl}/nh/bugs".lower())
        bugs = []
        for x in bugs_raw:
            bugs.append(Bug(x))
        return bugs
    
    async def getSeaCreature(self, name: str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/sea/{name}".lower())
        seaCreature = SeaCreature(data)
        return seaCreature
    
    async def getAllSeaCreatures(self):
        seaCreatures_raw = await self.fetchJson(f"{self.baseUrl}/nh/sea".lower())
        seaCreatures = []
        for x in seaCreatures_raw:
            seaCreatures.append(SeaCreature(x))
        return seaCreatures
    
    async def getArtwork(self, name: str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/art/{name}".lower())
        artwork = Artwork(data)
        return artwork
    
    async def getAllArtwork(self):
        artworks_raw = await self.fetchJson(f"{self.baseUrl}/nh/art".lower())
        artworks = []
        for x in artworks_raw:
            artworks.append(Artwork(x))
        return artworks
    
    async def getFossil(self, name: str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/fossils/individuals/{name}".lower())
        fossil = Fossil(data)
        return fossil
    
    async def getAllFossils(self):
        fossils_raw = await self.fetchJson(f"{self.baseUrl}/nh/fossils/individuals".lower())
        fossils = []
        for x in fossils_raw:
            fossils.append(Fossil(x))
        return fossils
    
    async def getFossilGroup(self, name: str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/fossils/groups/{name}".lower())
        fossilGroup = FossilGroup(data)
        return fossilGroup
    
    async def getAllFossilGroups(self):
        fossilGroups_raw = await self.fetchJson(f"{self.baseUrl}/nh/fossils/groups".lower())
        fossilGroups = []
        for x in fossilGroups_raw:
            fossilGroups.append(FossilGroup(x))
        return fossilGroups
    
    async def getFossilSet(self, name: str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/fossils/all/{name}".lower())
        fossilSet = FossilSet(data)
        return fossilSet
    
    async def getAllFossilSets(self):
        fossilSets_raw = await self.fetchJson(f"{self.baseUrl}/nh/fossils/all".lower())
        fossilSets = []
        for x in fossilSets_raw:
            fossilSets.append(FossilSet(x))
        return fossilSets
    
    async def getFurniture(self, name: str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/furniture/{name}".lower())
        furniture = Furniture(data)
        return furniture
    
    async def getAllFurniture(self):
        furniture_raw = await self.fetchJson(f"{self.baseUrl}/nh/furniture".lower())
        furniture = []
        for x in furniture_raw:
            furniture.append(Furniture(x))
        return furniture
    
    async def getClothing(self, name: str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/clothing/{name}".lower())
        clothing = Clothing(data)
        return clothing
    
    async def getAllClothing(self):
        clothing_raw = await self.fetchJson(f"{self.baseUrl}/nh/clothing".lower())
        clothing = []
        for x in clothing_raw:
            clothing.append(Clothing(x))
        return clothing
    
    async def getInteriorItem(self, name: str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/interior/{name}".lower())
        item = InteriorItem(data)
        return item
    
    async def getAllInteriorItems(self):
        items_raw = await self.fetchJson(f"{self.baseUrl}/nh/interior".lower())
        items = []
        for x in items_raw:
            items.append(InteriorItem(x))
        return items
    
    async def getTool(self, name: str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/tools/{name}".lower())
        tool = Tool(data)
        return tool
    
    async def getAllTools(self):
        tools_raw = await self.fetchJson(f"{self.baseUrl}/nh/tools".lower())
        tools = []
        for x in tools_raw:
            tools.append(Tool(x))
        return tools
    
    async def getPhoto(self, name:str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/photos/{name}".lower())
        photo = Photo(data)
        return photo
    
    async def getAllPhotos(self):
        photos_raw = await self.fetchJson(f"{self.baseUrl}/nh/photos".lower())
        photos = []
        for x in photos_raw:
            photos.append(Photo(x))
        return photos
    
    async def getMiscItem(self, name:str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/items/{name}".lower())
        item = MiscItem(data)
        return item
    
    async def getAllMiscItems(self):
        items_raw = await self.fetchJson(f"{self.baseUrl}/nh/items".lower())
        items = []
        for x in items_raw:
            items.append(MiscItem(x))
        return items
    
    async def getGyroid(self, name:str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/gyroids/{name}".lower())
        gyroid = Gyroid(data)
        return gyroid
    
    async def getAllGyroids(self):
        gyroids_raw = await self.fetchJson(f"{self.baseUrl}/nh/gyroids".lower())
        gyroids = []
        for x in gyroids_raw:
            gyroids.append(Gyroid(x))
        return gyroids
    
    async def getRecipe(self, name: str):
        data = await self.fetchJson(f"{self.baseUrl}/nh/recipes/{name}".lower())
        recipe = Recipe(data)
        return recipe
    
    async def getAllRecipes(self):
        recipes_raw = await self.fetchJson(f"{self.baseUrl}/nh/recipes".lower())
        recipes = []
        for x in recipes_raw:
            recipes.append(Recipe(x))
        return recipes
    
    async def getAllEvents(self):
        events_raw = await self.fetchJson(f"{self.baseUrl}/nh/events".lower())
        events = []
        for x in events_raw:
            events.append(Event(x))
        return events