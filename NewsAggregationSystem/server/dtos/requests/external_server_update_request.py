from pydantic import BaseModel
from typing import Optional

class ExternalServerUpdateRequest(BaseModel):
    api_key: Optional[str]
    base_url: Optional[str]
    is_active :Optional[bool]
    server_name: Optional[str]