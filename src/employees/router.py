# Write a class hiring_plan_router that will route requests to the appropriate handler, the class will user APIRouter from fastapi
# The paths will start with the prefix "/hiring_plan". It will handle the calls GET "/hiring_plan_name","/hiring_plan_name/graphs",
# POST "/hiring_plan_name/employees", DELETE "/hiring_plan_name/employees/employee_id", PUT "/hiring_plan_name/employees/employee_id" UPDATE "/hiring_plan_name/employees"

# Path: src/hiring_plan/router.py

from fastapi import APIRouter

class hiring_plan_router:
    def __init__(self):
        self.router = APIRouter(prefix='/hiring_plan')
        self.router.add_api_route('/{hiring_plan_name}', self.get_hiring_plan, methods=['GET'])
        self.router.add_api_route('/{hiring_plan_name}/graphs', self.get_graphs, methods=['GET'])
        self.router.add_api_route('/{hiring_plan_name}/employees', self.add_employee, methods=['POST'])
        self.router.add_api_route('/{hiring_plan_name}/employees/{employee_id}', self.employee_id, methods=['DELETE', 'PUT', 'UPDATE'])

    def get_hiring_plan(self):
        return {"name": "get"}

    def get_graphs(self):
        return {"name": "graphs"}

    def add_employee(self):
        return {"name": "employees"}

    def employee_id(self):
        return {"name": "employee_id"}
