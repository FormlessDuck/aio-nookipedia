class Fossil:
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
    def __init__(self, data: dict):
        self.name = data['name']
        self.url = data['url']
        self.room = data['room']
        self.description = data['description']

class FossilSet:
    def __init__(self, data: dict):
        self.name = data['name']
        self.url = data['url']
        self.room = data['room']
        self.description = data['description']
        self.fossils = []
        for fossil in data['fossils']:
            self.fossils.append(Fossil(fossil))
