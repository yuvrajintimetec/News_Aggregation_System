from pydantic import BaseModel
from typing import Optional

class ReactArticleRequest(BaseModel):
    is_like :bool