from jose import jwt, JWTError
from fastapi import Header, HTTPException

SECRET_KEY = "medscale-secret"
ALGORITHM = "HS256"

def create_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    return verify_token(token)