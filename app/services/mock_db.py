from typing import Dict, Any, List
import random
from datetime import datetime, timedelta
from app.core.config import settings

class MockDatabase:
    def __init__(self):
        self.data = self._generate_mock_data()
        
    async def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """
        Execute a mock query and return simulated results.
        """
        # In a real implementation, this would parse the SQL query
        # and execute it against a real database
        # For now, we'll return mock data based on the query intent
        if "sales" in query.lower():
            return self._get_sales_data()
        elif "performance" in query.lower():
            return self._get_performance_data()
        else:
            return self._get_generic_data()
    
    def _generate_mock_data(self) -> List[Dict[str, Any]]:
        """
        Generate mock data for testing.
        """
        data = []
        for i in range(settings.MOCK_DATASET_SIZE):
            data.append({
                "id": i,
                "timestamp": datetime.now() - timedelta(days=random.randint(0, 365)),
                "value": random.uniform(1000, 10000),
                "category": random.choice(["sales", "revenue", "profit", "cost"]),
                "region": random.choice(["north", "south", "east", "west"]),
                "product": random.choice(["product_a", "product_b", "product_c"])
            })
        return data
    
    def _get_sales_data(self) -> List[Dict[str, Any]]:
        """
        Return mock sales data.
        """
        return [
            {
                "date": "2024-Q1",
                "region": "north",
                "sales": random.uniform(50000, 100000),
                "growth": random.uniform(0.05, 0.15)
            },
            {
                "date": "2024-Q1",
                "region": "south",
                "sales": random.uniform(50000, 100000),
                "growth": random.uniform(0.05, 0.15)
            }
        ]
    
    def _get_performance_data(self) -> List[Dict[str, Any]]:
        """
        Return mock performance metrics.
        """
        return [
            {
                "metric": "revenue",
                "value": random.uniform(100000, 200000),
                "trend": random.choice(["up", "down", "stable"]),
                "period": "2024-Q1"
            },
            {
                "metric": "profit",
                "value": random.uniform(50000, 100000),
                "trend": random.choice(["up", "down", "stable"]),
                "period": "2024-Q1"
            }
        ]
    
    def _get_generic_data(self) -> List[Dict[str, Any]]:
        """
        Return generic mock data.
        """
        return random.sample(self.data, min(5, len(self.data))) 