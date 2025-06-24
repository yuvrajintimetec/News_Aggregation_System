from pydantic import BaseModel
from typing import Optional

class ExternalServerUpdateRequest(BaseModel):
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    is_active :Optional[bool] = None
    server_name: Optional[str] = None