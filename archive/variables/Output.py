class Output:
    def __init__(self, id: str, name: str, calc, type: str):
        self.id = id
        self.name = name
        self.calc = calc
        self.type = type

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_calc(self):
        return self.calc

    def set_calc(self, calc):
        self.calc = calc

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type
