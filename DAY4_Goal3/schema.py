from pydantic import BaseModel, Field
from typing import Optional

class DocumentExtractionSchema(BaseModel):
    document_type: str = Field(description="Type of document, e.g., PAN Card")
    full_name: Optional[str] = Field(description="Full name of the individual")
    id_number: Optional[str] = Field(description="Identification number (e.g., PAN number)")
    date_of_birth: Optional[str] = Field(description="Date of birth in DD/MM/YYYY format")
    confidence_score: float = Field(description="Confidence score between 0.0 and 1.0")
    extraction_notes: Optional[str] = Field(description="Notes on image quality and distortion handling")
