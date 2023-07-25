import datetime


class Employee:
    def __init__(self, id: str, full_name: str, title: str, start_date: datetime, end_date: datetime, yearly_salary:
    int, bonus: int, type: str):
        self.id = id
        self.full_name = full_name
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.yearly_salary = yearly_salary
        self.bonus = bonus
        self.type = type

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_full_name(self):
        return self.full_name

    def set_full_name(self, full_name):
        self.full_name = full_name

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def get_yearly_salary(self):
        return self.yearly_salary

    def set_yearly_salary(self, yearly_salary):
        self.yearly_salary = yearly_salary

    def get_bonus(self):
        return self.bonus

    def set_bonus(self, bonus):
        self.bonus = bonus

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type
