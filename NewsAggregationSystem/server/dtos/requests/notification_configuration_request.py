from pydantic import BaseModel
from typing import Optional

class NotificationConfigurationRequest(BaseModel):
    category: Optional[str] = None
    keyword: Optional[str] = None
    is_enabled :Optional[bool] = None