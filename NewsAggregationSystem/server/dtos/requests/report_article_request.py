from pydantic import BaseModel
from typing import Optional

class ReportArticleRequest(BaseModel):
    reason: str