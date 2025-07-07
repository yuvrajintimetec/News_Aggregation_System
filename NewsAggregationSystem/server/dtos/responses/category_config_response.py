from pydantic import BaseModel
from typing import Optional, List

class CategoryConfigurationResponse(BaseModel):
    category_name: str
    is_enabled: bool

class CategoryConfigResponse(BaseModel):
    message: Optional[List[CategoryConfigurationResponse]] = None
    error: Optional[str] = None
