from datetime import timedelta

from pydantic import BaseModel, Field


class Answer(BaseModel):
    """Model for an answer."""
    answer: str = Field(..., description="Answer text")
    summary: str = Field(..., description="Answer summary")
    confidence: float = Field(..., description="A number from 0 to 1")


class ModelResponse(BaseModel):
    """Model for ModelResponse"""
    response: str = Field(..., description="Substantive answer")
    model: str = Field(..., description="Used model")
    input_tokens: int = Field(..., description="Number of input tokens")
    output_tokens: int = Field(..., description="Number of output tokens")
    duration_ms: int = Field(..., description="Duration in milliseconds")
    request_id: str = Field(..., description="Request ID")
