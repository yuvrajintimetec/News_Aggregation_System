from pydantic import BaseModel
from typing import Optional

class ReactDislikeArticleRequest(BaseModel):
    is_dislike :bool