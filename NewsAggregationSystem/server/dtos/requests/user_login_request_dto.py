from pydantic import BaseModel, EmailStr

class UserSignInRequest(BaseModel):
    email: EmailStr
    password: str