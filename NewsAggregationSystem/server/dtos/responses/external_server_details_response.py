from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class ExternalServerDetailResponse(BaseModel):
    server_name: str
    api_key: str
    base_url: str
    is_active: bool
    last_accessed: datetime

class ExternalServerDetailsResponse(BaseModel):
    message: Optional[List[ExternalServerDetailResponse]] = None
    error: Optional[str] = None
