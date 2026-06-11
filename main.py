from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/protected")
def protected(authorization: str = Header(...)):
    return {"token": authorization}