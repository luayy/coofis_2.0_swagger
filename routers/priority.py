from fastapi import APIRouter

router = APIRouter()

@router.get('/nde/config/priority/v1/', tags=["config"])
def get_priority():
    return [
        {"id": "1", "priority": "Umum"},
        {"id": "2", "priority": "Rahasia"},
        {"id": "3", "priority": "Segera"},
    ]
