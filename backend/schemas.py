from pydantic import BaseModel, Field
from typing import Optional

class Lead(BaseModel):
    name: str = Field(..., description="Name of the lead")
    email: str = Field(..., description="Contact email")
    company: Optional[str] = Field(None, description="Company name")
    message: Optional[str] = Field(None, description="Message from lead")
