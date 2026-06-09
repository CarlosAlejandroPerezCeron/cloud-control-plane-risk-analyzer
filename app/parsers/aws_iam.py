from pydantic import BaseModel
from typing import List

class IAMStatement(BaseModel):
    Effect: str
    Action: List[str]
    Resource: List[str]

class IAMPolicy(BaseModel):
    Version: str
    Statement: List[IAMStatement]
