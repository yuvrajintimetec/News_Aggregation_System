from pydantic import BaseModel

class CreateCategoryRequest(BaseModel):
    category_name: str
