from typing import List, Dict
from schema import *

class Company(BaseModel):
    id: str
    name: str
    description: str
    field: str
    created_at: datetime


class User(BaseModel):
    id: str
    first_name: str
    last_name: str
    image: str
    role: str
    email: str
    companies: List[Company]
    created_at: datetime
    generated_outputs: Dict[str, Output]


class Forecast(BaseModel):
    company: Company
    id: str
    title: str
    is_main: bool
    start_date: datetime
    end_date: datetime
    created_at: datetime
    hiring_models: Dict[str, List[Employee]]



class Model(BaseModel):
    id: str
    forecast: Forecast
    title: str
    inputs: Input
    formulas: Dict[str, Formula]

