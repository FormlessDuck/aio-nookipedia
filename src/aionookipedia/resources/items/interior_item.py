from .item import Item

class InteriorItem(Item):
    __slots__ = (
        "image_url",
        "item_series",
        "item_set",
        "themes",
        "hha_category",
        "hha_base",
        "tag",
        "grid_width",
        "grid_length",
        "colors"
    )
    def __init__(self, data: dict):
        super().__init__(data)
        self.image_url = data['image_url']
        self.item_series = data['item_series']
        self.item_set = data['item_set']
        self.themes = data['themes']
        self.hha_category = data['hha_category']
        self.hha_base = data['hha_base']
        self.tag = data['tag']
        self.grid_width = data['grid_width']
        self.grid_length = data['grid_length']
        self.colors = data['colors']

