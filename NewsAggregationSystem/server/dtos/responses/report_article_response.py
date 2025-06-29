from pydantic import BaseModel
from datetime import datetime

class ReportArticleResponse(BaseModel):
    reported_article_id: int
    article_id: int
    user_id: int
    report_reason: str
    reported_at: datetime
