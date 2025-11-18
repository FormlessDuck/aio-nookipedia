from .items.item import Prices
from .items.item import Availability

class Recipe:
    __slots__ = (
        "name",
        "url",
        "image_url",
        "serial_id",
        "buy",
        "availability",
        "materials"
    )
    def __init__(self, data: dict):
        self.name = data['name']
        self.url = data['url']
        self.image_url = data['image_url']
        self.serial_id = data['serial_id']
        prices = []
        for x in data['buy']:
            prices.append(Prices(x))
        self.buy = prices
        availability = []
        for x in data['availability']:
            availability.append(Availability(x))
        self.availability = availability
        materials = []
        for x in data['materials']:
            materials.append(Material(x))
        self.materials = materials

class Material:
    __slots__ = (
        "name",
        "count"
    )
    def __init__(self, data: dict):
        self.name = data['name']
        self.count = data['count']
