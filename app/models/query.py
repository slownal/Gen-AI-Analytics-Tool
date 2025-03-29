from pydantic import BaseModel
from typing import Dict, Any, List, Optional
from datetime import datetime

class QueryRequest(BaseModel):
    query: str
    user_id: Optional[str] = None

class QueryResponse(BaseModel):
    query_id: str
    results: List[Dict[str, Any]]
    execution_time: float
    status: str
    timestamp: datetime = datetime.utcnow()

class QueryExplanation(BaseModel):
    query_id: str
    natural_language: str
    translated_query: str
    execution_plan: Dict[str, Any]
    estimated_cost: float

class QueryValidation(BaseModel):
    is_valid: bool
    message: str
    suggestions: Optional[List[str]] = None
    complexity_score: Optional[float] = None 