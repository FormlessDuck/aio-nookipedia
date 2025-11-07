from .item import Item

class Gyroid(Item):
    def __init__(self, data: dict):
        super().__init__(data)
        self.hha_base = data['hha_base']
        self.customizable = data['customizable']
        self.custom_kits = data['custom_kits']
        self.custom_body_part = data['custom_body_part']
        self.cyrus_price = data['cyrus_price']
        self.variation_total = data['variation_total']
        self.grid_width = data['grid_width']
        self.grid_length = data['grid_length']
        self.sound = data['sound']
