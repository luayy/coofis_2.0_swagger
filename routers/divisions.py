from fastapi import APIRouter

router = APIRouter()

@router.get("/nde/division/")
def get_division():
    return [
        {"Id": "1", "name": "EVP RKO"},
        {"Id": "2", "name": "ADT Commerce and CS"},
        {"Id": "3", "name": "EVP Kons Reg JBT"}
    ]
