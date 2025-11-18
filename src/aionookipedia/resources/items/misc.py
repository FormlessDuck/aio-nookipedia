from .item import Item

class MiscItem(Item):
    __slots__ = (
        "image_url",
        "stack",
        "hha_base",
        "is_fence",
        "material_type",
        "material_seasonality",
        "material_sort",
        "material_name_sort",
        "material_seasonailty_sort",
        "edible",
        "plant_type"
    )
    def __init__(self, data: dict):
        super().__init__(data)
        self.image_url = data['image_url']
        self.stack = data['stack']
        self.hha_base = data['hha_base']
        self.is_fence = data['is_fence']
        self.material_type = data['material_type']
        self.material_seasonality = data['material_seasonality']
        self.material_sort = data['material_sort']
        self.material_name_sort = data['material_name_sort']
        self.material_seasonailty_sort = data['material_seasonality_sort']
        self.edible = data['edible']
        self.plant_type = data['plant_type']
