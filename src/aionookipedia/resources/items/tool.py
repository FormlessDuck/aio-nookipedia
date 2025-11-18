from .item import Item

class Tool(Item):
    __slots__ = (
        "uses",
        "hha_base",
        "customizable",
        "custom_kits",
        "custom_body_part"
    )
    def __init__(self, data: dict):
        super().__init__(data)
        self.uses = data['uses']
        self.hha_base = data['hha_base']
        self.customizable = data['customizable']
        self.custom_kits = data['custom_kits']
        self.custom_body_part = data['custom_body_part']
        
