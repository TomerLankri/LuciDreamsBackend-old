import datetime

class Forecast:
    def __init__(self, company, id: str, title: str, is_main: bool, start_date: datetime, end_date: datetime, created_at: datetime, hiringModels):
        self.company = company
        self.id = id
        self.title = title
        self.is_main = is_main
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = created_at
        self.hiringModels = hiringModels

    def get_company(self):
        return self.company

    def set_company(self, company):
        self.company = company

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_is_main(self):
        return self.is_main

    def set_is_main(self, is_main):
        self.is_main = is_main

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def get_created_at(self):
        return self.created_at

    def set_created_at(self, created_at):
        self.created_at = created_at

    def get_hiringModels(self):
        return self.hiringModels

    def set_hiringModels(self, hiringModels):
        self.hiringModels = hiringModels

