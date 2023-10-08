from pydantic import BaseModel
from typing import Any, Optional


class Customers(BaseModel):
    id: Any
    image: str
    image_gray: Optional[str]
    name: str
    company: str
    message: str
    name_color: Optional[str]

    class Config:
        orm_mode = True
