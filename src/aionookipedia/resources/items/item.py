class Item:
    __slots__ = (
        "name",
        "url",
        "category",
        "unlocked",
        "sell",
        "version_added",
        "notes",
        "buy",
        "availability",
        "variations"
    )
    def __init__(self, data: dict):
        self.name = data['name']
        self.url = data['url']
        self.category = data['category'] if 'category' in data else None
        self.unlocked = data['unlocked'] if "unlocked" in data else None
        self.sell = data['sell']
        self.version_added = data['version_added']
        self.notes = data['notes'] if 'notes' in data else None
        prices = []
        for price in data['buy']:
            prices.append(Prices(price))
        self.buy = prices
        availability = []
        for x in data['availability']:
            availability.append(Availability(x))
        self.availability = availability
        if 'variations' in data:
            variations = []
            for x in data['variations']:
                variations.append(Variations(x))
            self.variations = variations if variations else None

class Availability:
    __slots__ = (
        "location",
        "note"
    )
    def __init__(self, data: dict):
        self.location = data['from']
        self.note = data['note']

class Variations:
    __slots__ = (
        "variation",
        "pattern",
        "image_url",
        "colors"
    )
    def __init__(self, data: dict):
        self.variation = data['variation']
        self.pattern = data['pattern'] if 'pattern' in data else None
        self.image_url = data['image_url']
        self.colors = data['colors'] if 'colors' in data else None

class Prices:
    __slots__ = (
        "price",
        "currency"
    )
    def __init__(self, data: dict):
        self.price = data['price'] if 'price' in data else None
        self.currency = data['currency'] if 'currency' in data else None