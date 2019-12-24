from fastapi import APIRouter

router = APIRouter()

@router.get("/inbox/")
def get_inboxes():
    return [
        {"nomor_surat": "32/AGA/None/2019-R", "sender": "Budi", "receiver": "Indah", "date": "24/12/2019", "body": "Tolong segera adakan kegiatan donor darah"},
        {"nomor_surat": "24/EVP/None/2019-R", "sender": "Eko", "receiver": "Achmad", "date": "23/12/2019", "body": "Pmeberitahuan cuti bersama Natal dan Tahun Baru 2019"},
    ]

@router.get("/inbox/{nomor_surat}")
def get_inbox_detail(id_surat: str):
    return {"body": "some important mail", "nomor_surat": id_surat}

@router.get("/inbox/send/")
def get_inbox_send():
    return [
        {"nomor_surat" : "01/CS/None/2019-R", "sender": "Fachrul",
        "receiver" : ["Indah", "Gading", "Bruno"], "date": "25/12/2019", "body": "Segera adakan agenda rapat bulanan"}
    ]
