'''
This file defines:

request and response schemas for FastAPI endpoints.

Schemas provide:

request validation
structured APIs
type safety
cleaner documentation
Swagger integration

This is standard backend engineering practice
'''

from pydantic import BaseModel


class IngestRequest(BaseModel):
    url: str


class ChatRequest(BaseModel):
    question: str