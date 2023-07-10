# Write a class financial_report_router that will route requests to the appropriate handler, the class will user APIRouter from fastapi
# The reports path will start with the prefix "/financial-report". It will handle a general get and a "/graphs" path
# both of the calls will return a json with their name in it

# Path: src/financial_report/router.py

from fastapi import APIRouter

class financial_report_router:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route('/', self.get, methods=['GET'])
        self.router.add_api_route('/graphs', self.graphs, methods=['GET'])

    def get(self):
        return {"name": "get"}

    def graphs(self):
        return {"name": "graphs"}
