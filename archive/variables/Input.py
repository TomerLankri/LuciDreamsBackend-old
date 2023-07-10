import Variable


class Input(Variable.Variable):
    def __init__(self, name: str, value: int):
        Variable.Variable.__init__(self, name, value, None, None)

    def calc(self, date):
        return self.value

    #add get and set methods for name and value
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type
