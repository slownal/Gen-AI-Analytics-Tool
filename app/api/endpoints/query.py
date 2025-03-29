from fastapi import APIRouter, HTTPException, Depends
from app.models.query import QueryRequest, QueryResponse
from app.services.query_processor import QueryProcessor
from app.core.security import get_current_user
from typing import Dict, Any

router = APIRouter()
query_processor = QueryProcessor()

@router.post("/", response_model=QueryResponse)
async def process_query(
    query_request: QueryRequest,
    current_user: Dict[str, Any] = Depends(get_current_user)
) -> QueryResponse:
    """
    Process a natural language query and return the results.
    """
    try:
        # Process the query
        result = await query_processor.process_query(
            query=query_request.query,
            user_id=current_user["id"]
        )
        
        return QueryResponse(
            query_id=result["query_id"],
            results=result["data"],
            execution_time=result["execution_time"],
            status="success"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing query: {str(e)}"
        ) 