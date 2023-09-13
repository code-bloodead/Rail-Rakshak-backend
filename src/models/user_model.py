from pydantic import BaseModel
from fastapi import Form

class User(BaseModel):
    fullname: str = Form(...)
    password: str = Form(...)
    mobile: str = Form(...)
    otp: str = Form(default="")
    is_verified: str = Form(default=False)
    active: bool = Form(default=False)

class UserLogin(BaseModel):
    mobile: str = Form(...)
    password: str = Form(...)
    otp: str = Form(default="")

class UserToken(BaseModel):
    access_token: str = Form(...)
    token_type: str = Form(...)

class TokenData(BaseModel):
    mobile: str or None = None