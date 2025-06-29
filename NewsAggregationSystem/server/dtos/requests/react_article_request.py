from pydantic import BaseModel
from typing import Optional

class ReactArticleRequest(BaseModel):
    article_id: int
    is_like :bool