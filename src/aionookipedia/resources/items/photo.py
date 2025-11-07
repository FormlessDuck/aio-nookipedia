from .item import Item

class Photo(Item):
    def __init__(self, data: dict):
        super().__init__(data)
        self.customizable = data['customizable']
        self.custom_kits = data['custom_kits']
        self.custom_body_part = data['custom_body_part']
        self.grid_width = data['grid_width']
        self.grid_length = data['grid_length']
        self.interactable = data['interactable']
