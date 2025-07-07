from pydantic import BaseModel
from typing import Optional, List

class CategoryDetailResponse(BaseModel):
    category_id: int
    category_name: str

class CategoryDetailsResponse(BaseModel):
    message: Optional[List[CategoryDetailResponse]] = None
    error: Optional[str] = None
