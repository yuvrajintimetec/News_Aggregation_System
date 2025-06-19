from pydantic import BaseModel
from datetime import datetime

class ExternalServerResponseDTO(BaseModel):
    server_name: str
    is_active: bool
    last_accessed: datetime | None
