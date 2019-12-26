from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Profile(BaseModel):
    full_name: str
    jabatan: str
    profile_image: str

@router.get("/nde/profile/")
def get_profile():
    return [
        {
        "id": "1",
        "full_name": "Achmad Hartanto",
        "jabatan": "EVP RKO",
        "profile_image": "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"
        }
    ]

@router.put("/update-profile/")
async def update_profile(profile:Profile):
    return {**profile.dict()}
