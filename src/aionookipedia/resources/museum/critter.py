class Critter:
    def __init__(self, data: dict):
        self.url = data["url"]
        self.name = data["name"]
        self.image_url = data["image_url"]
        self.catchphrases = data["catchphrases"]
        self.rarity =  data["rarity"]
        self.total_catch = data["total_catch"]
        self.sell_nook = data["sell_nook"]
        self.tank_width = data["tank_width"]
        self.tank_length = data["tank_length"]
        self.north = HemisphereDetails(data["north"])
        self.south = HemisphereDetails(data["south"])

class HemisphereDetails:
    def __init__(self, data: dict):
        self.availabiliy_array = []
        for x in data["availability_array"]:
            self.availabiliy_array.append(AvailabilityDetails(x))
        self.months = data["months"]
        self.times_by_month = data["times_by_month"]
        self.months_array = data["months_array"]

    

class AvailabilityDetails:
    def __init__(self, data: dict):
        self.months = data["months"]
        self.time = data["time"]
