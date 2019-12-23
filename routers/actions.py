from fastapi import APIRouter

router = APIRouter()

@router.get("/action/")
def read_action():
    return [
        {"Id": "1", "name": "Approve"},
        {"Id": "2", "name": "Reject"},
        {"Id": "3", "name": "Return"},
    ]
