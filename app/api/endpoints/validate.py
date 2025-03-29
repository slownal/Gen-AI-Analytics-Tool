from fastapi import APIRouter, HTTPException, Depends
from app.models.query import QueryRequest, QueryValidation
from app.core.security import get_current_user
from typing import Dict, Any

router = APIRouter()

@router.post("/", response_model=QueryValidation)
async def validate_query(
    query_request: QueryRequest,
    current_user: Dict[str, Any] = Depends(get_current_user)
) -> QueryValidation:
    """
    Validate a natural language query before execution.
    """
    try:
        # Basic validation logic
        query = query_request.query.lower()
        
        # Check for empty queries
        if not query.strip():
            return QueryValidation(
                is_valid=False,
                message="Query cannot be empty",
                suggestions=["Please provide a valid query"]
            )
        
        # Check for minimum length
        if len(query.split()) < 3:
            return QueryValidation(
                is_valid=False,
                message="Query is too short",
                suggestions=["Please provide more details in your query"]
            )
        
        # Check for supported keywords
        supported_keywords = ["show", "display", "find", "get", "calculate", "compare"]
        has_supported_keyword = any(keyword in query for keyword in supported_keywords)
        
        if not has_supported_keyword:
            return QueryValidation(
                is_valid=False,
                message="Query must start with a supported keyword",
                suggestions=[f"Try starting with: {', '.join(supported_keywords)}"]
            )
        
        # If all validations pass
        return QueryValidation(
            is_valid=True,
            message="Query is valid and can be processed",
            complexity_score=0.7
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error validating query: {str(e)}"
        ) 