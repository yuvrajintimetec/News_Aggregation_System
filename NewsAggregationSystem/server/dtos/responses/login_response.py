from pydantic import BaseModel
from typing import Optional

class LoginResponse(BaseModel):
    message: Optional[str] = None
    access_token: Optional[str] = None
    error: Optional[str] = None

