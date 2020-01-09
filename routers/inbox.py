from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Inbox(BaseModel):
    no_agenda: str
    receive_date: str
    no_surat: str
    date: str
    sender: str
    receiver: str
    copytos: str = None
    subject: str
    priority: str
    type: str
    desc: str

@router.get("/nde/mail/inbox", tags=["mail"])
def get_inboxes():
    return [
        {"nomor_surat": "32/AGA/None/2019-R", "sender": "Budi", "receiver": "Indah", "date": "24/12/2019", "body": "Tolong segera adakan kegiatan donor darah"},
        {"nomor_surat": "24/EVP/None/2019-R", "sender": "Eko", "receiver": "Achmad", "date": "23/12/2019", "body": "Pmeberitahuan cuti bersama Natal dan Tahun Baru 2019"},
    ]

@router.get("/nde/mail/inbox/{nomor_surat}", tags=["mail"])
def get_inbox_detail(id_surat: str):
    return {"body": "some important mail", "nomor_surat": id_surat}

@router.get("/nde/mail/inbox/send", tags=["mail"])
def get_inbox_send():
    return [
        {"nomor_surat" : "01/CS/None/2019-R", "sender": "Fachrul",
        "receiver" : ["Indah", "Gading", "Bruno"], "date": "25/12/2019", "body": "Segera adakan agenda rapat bulanan"}
    ]

@router.post("/nde/mail/inbox", tags=["mail"])
async def create_inbox(inbox:Inbox):
    return inbox
