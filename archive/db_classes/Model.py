import Forecast
from archive.variables import Input


class Model:
    def __init__(self, id: str, forecast: Forecast, title: str, inputs: Input, formulas: dict):
        self.id = id
        self.forecast = forecast
        self.title = title
        self.inputs = inputs
        self.formulas = formulas

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_forecast(self):
        return self.forecast

    def set_forecast(self, forecast):
        self.forecast = forecast

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_inputs(self):
        return self.inputs

    def set_inputs(self, inputs):
        self.inputs = inputs

    def get_formulas(self):
        return self.formulas

    def set_formulas(self, formulas):
        self.formulas = formulas
