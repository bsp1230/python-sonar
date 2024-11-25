from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI application!"}

@app.get("/items/{item_id}")
def readItem(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
