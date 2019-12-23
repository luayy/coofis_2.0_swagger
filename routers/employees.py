from fastapi import APIRouter

router = APIRouter()

@router.get("/employee/")
def read_employee():
    return [
        {"Id": "1", "name": "Achmad"},
        {"Id": "2", "name": "Budi"},
        {"Id": "3", "name": "Caca"}
    ]
