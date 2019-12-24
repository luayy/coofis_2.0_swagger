from fastapi import APIRouter

router = APIRouter()

@router.get("/employee/")
def get_employee():
    return [
        {"Id": "1", "name": "Achmad"},
        {"Id": "2", "name": "Budi"},
        {"Id": "3", "name": "Caca"}
    ]

@router.get("/employee/{name}")
def get_employee_detail(nama: str):
    return {
        "ide": "1",
        "full_name": "Achmad Hartanto",
        "nick_name": "Achmad",
        "division": "EVP RKO",
        "address": "Jl. Pemuda No. 12",
        "city": "Bandung",
        "phone": "089567112304"
    }
