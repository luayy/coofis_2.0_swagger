from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel
from routers import divisions, employees, actions, inbox, profile

app = FastAPI()

app.include_router(divisions.router)
app.include_router(employees.router)
app.include_router(actions.router)
app.include_router(inbox.router)
app.include_router(profile.router)
