from fastapi import APIRouter

router = APIRouter()

@router.get('/priority/')
def get_priority():
    return [
        {"id": "1", "priority": "Umum"},
        {"id": "2", "priority": "Rahasia"},
        {"id": "3", "priority": "Segera"},
    ]
