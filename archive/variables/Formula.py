from archive.variables import Input


class Formula(Input):
    def __init__(self, name: str, value, data: dict):
        Input.__init__(self, name, value)
        self.data = data

    def calc(self, date):
        return self.value
