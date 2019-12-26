from fastapi import APIRouter

router = APIRouter()

@router.get("/nde/action/")
def get_action():
    return [
        {"Id": "1", "name": "Approve"},
        {"Id": "2", "name": "Reject"},
        {"Id": "3", "name": "Return"},
    ]
