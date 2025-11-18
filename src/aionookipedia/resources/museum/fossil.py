class Fossil:
    __slots__ = (
        "name",
        "url",
        "image_url",
        "fossil_group",
        "interactable",
        "sell",
        "hha_base",
        "width",
        "length",
        "colors"
    )
    def __init__(self, data: dict):
        self.name = data['name']
        self.url = data['url']
        self.image_url = data['image_url']
        self.fossil_group = data['fossil_group'] if 'fossil_group' in data else None
        self.interactable = data['interactable']
        self.sell = data['sell']
        self.hha_base = data['hha_base']
        self.width = data['width']
        self.length = data['length']
        self.colors = data['colors']

class FossilGroup:
    __slots__ = (
        "name",
        "url",
        "room",
        "description"
    )
    def __init__(self, data: dict):
        self.name = data['name']
        self.url = data['url']
        self.room = data['room']
        self.description = data['description']

class FossilSet:
    __slots__ = (
        "name",
        "url",
        "room",
        "description",
        "fossils"
    )
    def __init__(self, data: dict):
        self.name = data['name']
        self.url = data['url']
        self.room = data['room']
        self.description = data['description']
        self.fossils = []
        for fossil in data['fossils']:
            self.fossils.append(Fossil(fossil))
