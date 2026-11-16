from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field

class InvoiceStatus(str, Enum):
    PAID = "PAID"
    PENDING = "PENDING"
    OVERDUE = "OVERDUE"
    CANCELLED = "CANCELLED"

class Address(BaseModel):
    street: str = Field(description="Street address including building number")
    city: str = Field(description="City name")
    pin_code: str = Field(description="Postal or ZIP code")

class LineItem(BaseModel):
    item_description: str = Field(description="Description of the product or service")
    quantity: int = Field(description="Quantity purchased")
    unit_price: float = Field(description="Price per unit in USD or INR")
    total_price: float = Field(description="Total price for this line item")

class InvoiceExtractionSchema(BaseModel):
    invoice_number: str = Field(description="Unique invoice identifier")
    vendor_name: str = Field(description="Name of the company issuing the invoice")
    customer_name: str = Field(description="Name of the client or customer")
    invoice_date: str = Field(description="Date of invoice issuance (YYYY-MM-DD)")
    status: InvoiceStatus = Field(description="Current payment status")
    billing_address: Address = Field(description="Nested billing address object")
    line_items: List[LineItem] = Field(description="List of purchased line items")
    discount_applied: Optional[float] = Field(default=None, description="Optional discount amount if applied")
    total_amount: float = Field(description="Final total payable amount")
