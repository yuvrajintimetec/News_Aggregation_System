from pydantic import BaseModel
from datetime import datetime

class UserDetailsResponse(BaseModel):
    name: str
    user_role: str
