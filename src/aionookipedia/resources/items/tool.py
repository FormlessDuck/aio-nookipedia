from .item import Item

class Tool(Item):
    def __init__(self, data: dict):
        super().__init__(data)
        self.uses = data['uses']
        self.hha_base = data['hha_base']
        self.customizable = data['customizable']
        self.custom_kits = data['custom_kits']
        self.custom_body_part = data['custom_body_part']
        
