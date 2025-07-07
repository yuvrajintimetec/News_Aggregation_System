from pydantic import BaseModel
from typing import Optional, List

class NotificationDetailsResponse(BaseModel):
    message: Optional[List[str]] = None
    error: Optional[str] = None
