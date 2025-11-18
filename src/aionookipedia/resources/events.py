class Event:
    __slots__ = (
        "name",
        "date",
        "type",
        "url"
    )
    def __init__(self, data: dict):
        self.name = data['event']
        self.date = data['date']
        self.type = data['type']
        self.url = data['url']