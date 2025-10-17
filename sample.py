from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import Base, engine, get_db
import models, schemas, crud
from auth import verify_password, create_access_token, SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from auth import verify_password, create_access_token, SECRET_KEY, ALGORITHM


# Tables create
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Blog App")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
def root():
    return{"message": "Welcome to FastAPI Blog App"}


@app.get("/register",response_model=schemas.UserResponse)
