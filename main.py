from fastapi import FastAPI

app = FastAPI()

@app.get("/getcode")
def get_code():
    return {"code": "123ABC"}

@app.get("/plus/{a}/{b}")
def plus(a: int, b: int):
    return {"result": a + b}
