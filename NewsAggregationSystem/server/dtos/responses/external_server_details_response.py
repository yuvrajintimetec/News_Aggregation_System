from pydantic import BaseModel
from datetime import datetime

class ExternalServerDetailsResponse(BaseModel):
    server_name: str
    api_key: str
    base_url: str
    is_active: bool
    last_accessed: datetime
