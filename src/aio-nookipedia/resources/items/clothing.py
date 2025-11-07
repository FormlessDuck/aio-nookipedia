from .item import Item

class Clothing(Item):
    def __init__(self, data: dict):
        super().__init__(data)
        self.variation_total = data['variation_total']
        self.vill_equip = data['vill_equip']
        self.seasonality = data['seasonality']
        self.notes = data['notes']
        self.label_themes = data['label_themes']
        self.styles = data['styles']
        