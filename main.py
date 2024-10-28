from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def getIndex():
    return {"Hello": "miks"}