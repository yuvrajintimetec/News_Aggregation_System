from pydantic import BaseModel
from typing import Optional

class ReactLikeArticleRequest(BaseModel):
    is_like :bool