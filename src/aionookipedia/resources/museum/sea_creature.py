from .critter import Critter

class SeaCreature(Critter):
    __slots__ = (
        "shadow_size",
        "shadow_movement"
    )
    def __init__(self, data: dict):
        super().__init__(data)
        self.shadow_size = data["shadow_size"]
        self.shadow_movement = data["shadow_movement"]