from pydantic import BaseModel, EmailStr

class UserRegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str