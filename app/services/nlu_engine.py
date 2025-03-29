from typing import Dict, Any
import re

class NLUEngine:
    def __init__(self):
        # Define basic patterns for intent recognition
        self.patterns = {
            "sales": r"(sales|revenue|income|earnings)",
            "performance": r"(performance|metrics|kpi|key performance)",
            "time": r"(quarter|q[1-4]|year|month|week)",
            "comparison": r"(compare|versus|vs|against)",
            "aggregation": r"(sum|total|average|mean|count)"
        }
        
    async def process_query(self, query: str) -> Dict[str, Any]:
        """
        Process a natural language query to extract intent and entities.
        """
        # Convert query to lowercase for pattern matching
        query_lower = query.lower()
        
        # Extract intents based on patterns
        intents = []
        for intent, pattern in self.patterns.items():
            if re.search(pattern, query_lower):
                intents.append(intent)
        
        # Extract time-related entities
        time_entities = self._extract_time_entities(query)
        
        # Extract comparison entities
        comparison_entities = self._extract_comparison_entities(query)
        
        return {
            "intent": intents[0] if intents else "unknown",
            "sub_intents": intents[1:] if len(intents) > 1 else [],
            "time_entities": time_entities,
            "comparison_entities": comparison_entities,
            "original_query": query
        }
    
    def _extract_time_entities(self, query: str) -> Dict[str, Any]:
        """
        Extract time-related entities from the query.
        """
        time_patterns = {
            "quarter": r"q[1-4]|quarter",
            "year": r"\b20\d{2}\b",
            "month": r"\b(january|february|march|april|may|june|july|august|september|october|november|december)\b",
            "week": r"week"
        }
        
        entities = {}
        for entity_type, pattern in time_patterns.items():
            match = re.search(pattern, query.lower())
            if match:
                entities[entity_type] = match.group(0)
        
        return entities
    
    def _extract_comparison_entities(self, query: str) -> Dict[str, Any]:
        """
        Extract comparison-related entities from the query.
        """
        comparison_patterns = {
            "metric": r"\b(sales|revenue|profit|cost|growth)\b",
            "time_period": r"\b(previous|last|current|this)\b"
        }
        
        entities = {}
        for entity_type, pattern in comparison_patterns.items():
            match = re.search(pattern, query.lower())
            if match:
                entities[entity_type] = match.group(0)
        
        return entities 