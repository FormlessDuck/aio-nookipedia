from .critter import Critter

class Bug(Critter):
    def __init__(self, data: dict):
        super().__init__(data)
        self.location = data["location"]
        self.sell_flick = data["sell_flick"]
        self.weather = data["weather"]