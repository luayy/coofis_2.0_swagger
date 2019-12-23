from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"Desc": "This is a documentation of Coofis 2.0 API"}


@app.get("/division-list")
def read_item():
    return [{"Id": "1", "name": "EVP RKO"},
    {"Id": "2", "name": "ADT Commerce and CS"},
    {"Id": "3", "name": "EVP Kons Reg JBT"}]
