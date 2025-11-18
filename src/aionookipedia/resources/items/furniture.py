from .item import Item

class Furniture(Item):
    __slots__ = (
        "item_series",
        "item_set",
        "themes",
        "hha_category",
        "hha_base",
        "tag",
        "lucky",
        "lucky_season",
        "variation_total",
        "pattern_total",
        "customizable",
        "custom_kits",
        "custom_kit_type",
        "custom_body_part",
        "custom_pattern_part",
        "grid_width",
        "grid_length",
        "height",
        "door_decor",
        "functions",
        "notes"
    )
    def __init__(self, data: dict):
        super().__init__(data)
        self.item_series = data['item_series']
        self.item_set = data['item_set']
        self.themes = data['themes']
        self.hha_category = data['hha_category']
        self.hha_base = data['hha_base']
        self.tag = data['tag']
        self.lucky = data['lucky']
        self.lucky_season = data['lucky_season'] if 'lucky_season' in data else None
        self.variation_total = data['variation_total']
        self.pattern_total = data['pattern_total']
        self.customizable = data['customizable']
        self.custom_kits = data['custom_kits'] if 'custom_kits' in data else None
        self.custom_kit_type = data['custom_kit_type'] if 'custom_kit_type' in data else None
        self.custom_body_part = data['custom_body_part']  if 'custom_body_part' in data else None
        self.custom_pattern_part = data['custom_pattern_part'] if 'custom_pattern_part' in data else None
        self.grid_width = data['grid_width']
        self.grid_length = data['grid_length']
        self.height = data['height']
        self.door_decor = data['door_decor']
        self.functions = data['functions']
        self.notes = data['notes']


