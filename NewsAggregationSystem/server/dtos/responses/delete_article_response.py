from pydantic import BaseModel
from typing import Optional

class DeleteArticleResponse(BaseModel):
    message: Optional[str] = None
    error: Optional[str] = None
