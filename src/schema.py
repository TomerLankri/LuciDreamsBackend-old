from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import List, Dict
from models import *


class Output(BaseModel):
    id: str
    name: str
    type: str


class Variable(BaseModel):
    id: str
    name: str
    value: str

    def calc(self):
        return self.value


class Input(Variable):
    calc: str
    type: str


class Formula(BaseModel):
    id: str
    name: str
    output: Output
    data: Dict[str, List[Variable]]

    def calc(self):
        return True

    @field_validator("data")
    def validate_data(cls, data: Dict[str, List[Variable]]) -> Dict[str, List[Variable]]:
        for key, value in data.items():
            if len(value) == 0:
                raise ValueError(f"Formula data for key '{key}' must not be empty.")
        return data


class Employee(BaseModel):
    id: str
    full_name: str
    title: str
    start_date: datetime
    end_date: datetime
    yearly_salary: int
    bonus: int
    type: str
