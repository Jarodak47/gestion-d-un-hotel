from pydantic import BaseModel
from typing import Any, List


class DataList(BaseModel):
    total: int
    pages: int
    current_page: int
    per_page: int
    data: List[Any] = []

    class Config:
        orm_mode = True
