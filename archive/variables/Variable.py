class Variable:
    def __init__(self, name:str, value:int,
                 id: str, type):
        self.name = name
        self.value = value
        self.id = id
        self.type = type

    def calc(self, date):
        return self.value