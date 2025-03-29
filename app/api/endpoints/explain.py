from fastapi import APIRouter, HTTPException, Depends
from app.models.query import QueryExplanation
from app.core.security import get_current_user
from typing import Dict, Any

router = APIRouter()

@router.get("/", response_model=QueryExplanation)
async def explain_query(
    query_id: str,
    current_user: Dict[str, Any] = Depends(get_current_user)
) -> QueryExplanation:
    """
    Explain a previously executed query.
    """
    try:
        # In a real implementation, this would fetch the query details from a database
        # For now, we'll return mock data
        return QueryExplanation(
            query_id=query_id,
            natural_language="Show me sales performance by region for Q1 2024",
            translated_query="SELECT * FROM sales WHERE quarter = 'Q1' AND year = 2024",
            execution_plan={
                "steps": [
                    {"operation": "scan", "table": "sales"},
                    {"operation": "filter", "condition": "quarter = 'Q1'"},
                    {"operation": "filter", "condition": "year = 2024"}
                ]
            },
            estimated_cost=0.5
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error explaining query: {str(e)}"
        ) 