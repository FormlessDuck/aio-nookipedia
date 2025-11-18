from .critter import Critter

class Bug(Critter):
    __slots__ = (
        "location",
        "sell_flick",
        "weather"
    )
    def __init__(self, data: dict):
        super().__init__(data)
        self.location = data["location"]
        self.sell_flick = data["sell_flick"]
        self.weather = data["weather"]