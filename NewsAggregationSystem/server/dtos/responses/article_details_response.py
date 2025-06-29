from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ArticleDetailsResponse(BaseModel):
    article_id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None
    source: Optional[str] = None
    url: Optional[str] = None
    published_at: datetime | None
    server_id : Optional[int] = None
