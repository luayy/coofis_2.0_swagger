from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"Desc": "This is a documentation of Coofis 2.0 API"}


@app.get("/division-list")
def read_item():
    return [
        {"Id": "1", "name": "EVP RKO"},
        {"Id": "2", "name": "ADT Commerce and CS"},
        {"Id": "3", "name": "EVP Kons Reg JBT"}
    ]

@app.get("/employee-list")
def read_item():
    return [
        {"Id": "1", "name": "Achmad"},
        {"Id": "2", "name": "Budi"},
        {"Id": "3", "name": "Caca"}
    ]

@app.get("/action-list")
def read_item():
    return [
        {"Id": "1", "name": "Approve"},
        {"Id": "2", "name": "Reject"},
        {"Id": "3", "name": "Return"},
    ]
