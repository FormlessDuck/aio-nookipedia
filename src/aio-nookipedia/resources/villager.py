class Villager:
    def __init__(self, data: dict):
        self.id = data["id"]
        self.url = data["url"]
        self.name = data["name"]
        self.alt_name = data["alt_name"]
        self.title_color = data["title_color"]
        self.text_color = data["text_color"]
        self.image_url = data["image_url"]
        self.species = data["species"]  
        self.personality = data["personality"]
        self.gender = data["gender"]
        self.birthday_day = data["birthday_day"]
        self.birthday_month = data["birthday_month"]
        self.sign = data["sign"]
        self.quote = data["quote"]
        self.phrase = data["phrase"]
        self.prev_phrases = data["prev_phrases"]
        self.clothing = data["clothing"]
        self.islander = data["islander"]
        self.debut = data["debut"]
        self.appearances = data["appearances"]
        self.nh_details = NHDetails(data["nh_details"]) if data['nh_details'] is not None else None

    @property
    def birthday(self) -> str:
        return f"{self.birthday_month} {self.birthday_day}"

      
class NHDetails:
    def __init__(self, data: dict):
        self.photo_url = data["photo_url"]
        self.image_url = data["image_url"]
        self.icon_url = data["icon_url"]
        self.quote = data["quote"]
        self.sub_personality = data["sub-personality"]
        self.catchphrase = data["catchphrase"]
        self.clothing = data["clothing"]
        self.clothing_variation = data["clothing_variation"]
        self.fav_styles = data["fav_styles"]
        self.hobby = data["hobby"]
        self.house_interior_url = data["house_interior_url"]
        self.house_exterior_url = data["house_exterior_url"]
        self.house_wallpaper = data["house_wallpaper"]
        self.house_flooring = data["house_flooring"]
        self.house_music = data["house_music"]
        self.house_music_note = data["house_music_note"]
        self.umbrella = data["umbrella"]
