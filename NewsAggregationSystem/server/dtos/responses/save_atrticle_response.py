from pydantic import BaseModel
from typing import Optional

class SaveArticleResponse(BaseModel):
    message: Optional[str] = None
    error: Optional[str] = None
