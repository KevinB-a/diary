class Event():
    """"""

    def __init__(self, data):
        self.id_event = None
        self.title = None
        self.date = None
        self.time = None
        self.description = None
        if data:
            self.hydrate(data)

    def hydrate(self, data):
        """ """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def show_event(self):
        try :
        return """_____________________________
        {} : {}
        {}
                _____________________________""".format(self.time, self.title, self.description)