from fastapi import APIRouter

router = APIRouter()

@router.get("/inbox/")
def read_inbox():
    return [
        {"Id": "1", "sender": "Budi", "receiver": "Indah", "date": "24/12/2019", "body": "Tolong segera adakan kegiatan donor darah"},
        {"Id": "2", "sender": "Eko", "receiver": "Achmad", "date": "23/12/2019", "body": "Pmeberitahuan cuti bersama Natal dan Tahun Baru 2019"},
    ]
