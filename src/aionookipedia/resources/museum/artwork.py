class Artwork:
    __slots__ = (
        "name",
        "url",
        "has_fake",
        "art_name",
        "art_type",
        "author",
        "year",
        "art_style",
        "buy",
        "sell",
        "availability",
        "width",
        "length",
        "real_info",
        "fake_info"
    )
    def __init__(self, data: dict):
        self.name = data['name']
        self.url = data['url']
        self.has_fake = data['has_fake']
        self.art_name = data['art_name']
        self.art_type = data['art_type']
        self.author = data['author']
        self.year = data['year']
        self.art_style = data['art_style']
        self.buy = data['buy']
        self.sell = data['sell']
        self.availability = data['availability']
        self.width = data['width']
        self.length = data['length']
        self.real_info = ArtworkInfo(data['real_info'])
        self.fake_info = ArtworkInfo(data['fake_info']) if self.has_fake else None

class ArtworkInfo:
    __slots__ = (
        "image_url",
        "texture_url",
        "description"
    )
    def __init__(self, data: dict):
        self.image_url = data['image_url']
        self.texture_url = data['texture_url']
        self.description = data['description']