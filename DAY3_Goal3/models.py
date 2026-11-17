from pydantic import BaseModel, EmailStr, Field

class Address(BaseModel):
    city: str = Field(..., description="City name")
    pincode: str = Field(..., description="6-digit postal code")

class ContactCard(BaseModel):
    name: str = Field(..., description="Full name of the person")
    email: EmailStr = Field(..., description="Valid email address")
    phone: str = Field(..., description="10-digit phone number without country code")
    address: Address = Field(..., description="Nested address object")
