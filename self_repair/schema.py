from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Address(BaseModel):
    city: str = Field(description="City name")
    pincode: str = Field(description="Postal or pincode")

class ContactCard(BaseModel):
    name: str = Field(description="Full name of the contact")
    email: EmailStr = Field(description="Valid email address")
    phone: str = Field(description="10-digit phone number")
    address: Address = Field(description="Nested address object with city and pincode")
