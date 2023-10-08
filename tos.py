from typing import Any, Optional

from pydantic import BaseModel, Field


class TermsOfServiceBase(BaseModel):
    title: str = Field(max_length=300, title='عنوان')
    content: str = Field(title='توضیحات')
    priority: Optional[int]

    class Config:
        orm_mode = True


class TermsOfService(TermsOfServiceBase):
    id: Any

    class Config:
        orm_mode = True
