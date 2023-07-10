import datetime

class Company:
    def __init__(self, id: str, name: str, description: str, field: str, created_at: datetime):
        self.id = id
        self.name = name
        self.description = description
        self.field = field
        self.created_at = created_at

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_field(self):
        return self.field

    def set_field(self, field):
        self.field = field

    def get_created_at(self):
        return self.created_at

    def set_created_at(self, created_at):
        self.created_at = created_at
