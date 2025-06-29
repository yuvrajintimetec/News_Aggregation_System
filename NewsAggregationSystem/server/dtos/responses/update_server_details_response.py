from pydantic import BaseModel
from typing import  Optional

class UpdateServerDetailsResponse(BaseModel):
    message: Optional[str] = None
    error: Optional[str] = None
