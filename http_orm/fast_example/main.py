from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def hello():
    return {"message": "hello world"}

@app.post("/create")
def create():
    return {"message": "create"}

@app.delete("/delete")
def delete():
    return {"message": "deleted"}