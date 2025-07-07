from pydantic import BaseModel

class CreateKeywordRequest(BaseModel):
    keyword: str
