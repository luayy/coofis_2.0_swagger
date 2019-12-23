from fastapi import Depends, FastAPI, Header, HTTPException
from routers import divisions, employees, actions, inbox

app = FastAPI()

app.include_router(divisions.router)
app.include_router(employees.router)
app.include_router(actions.router)
app.include_router(inbox.router)
