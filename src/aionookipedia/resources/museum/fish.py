from .critter import Critter

class Fish(Critter):
    __slots__ = (
        "shadow_size",
        "sell_cj",
        "location"
    )
    def __init__(self, data: dict):
        super().__init__(data)
        self.shadow_size = data["shadow_size"]
        self.sell_cj = data["sell_cj"]
        self.location = data["location"]