import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Email(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    subject: str = Field(...)
    message: str = Field(...)
    sender: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "email":{
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "subject": "Test Email",
                "message": "Email from test sending regards",
                "sender": "Jack MeHoff"
            }
        }

class EmailUpdate(BaseModel):
    title: Optional[str]
    subject: str = Field(...)
    message: str = Field(...)
    sender: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "subject": "Updated Test Email Subject",
                "message": "Updated Test Email Message",
                "sender": "Jack MeHoff"
            }
        }