from fastapi import APIRouter

router = APIRouter()

@router.get("/nde/config/action", tags=["config"])
def get_action():
    return [
        {"Id": "1", "name": "Approve"},
        {"Id": "2", "name": "Reject"},
        {"Id": "3", "name": "Return"},
    ]
