from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Employee(BaseModel):
    full_name: str
    nick_name: str
    division: str
    address: str
    city: str
    phone: str

@router.get("/nde/employee", tags=["employee"])
def get_employee():
    return [
        {"id": "1", "name": "Achmad"},
        {"id": "2", "name": "Budi"},
        {"id": "3", "name": "Caca"}
    ]

@router.get("/nde/employee/{name}", tags=["employee"])
def get_employee_detail(nama: str):
    return {
        "id": "1",
        "full_name": "Achmad Hartanto",
        "nick_name": "Achmad",
        "division": "EVP RKO",
        "address": "Jl. Pemuda No. 12",
        "city": "Bandung",
        "phone": "089567112304"
    }

@router.post("/nde/employee", tags=["employee"])
async def create_employee(employee: Employee):
    return employee

@router.put("/nde/employee/{id}", tags=["employee"])
async def update_employee(employee_id: int, employee: Employee):
    return {"employee_id": employee_id, **employee.dict()}
