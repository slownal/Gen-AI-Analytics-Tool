# Gen AI Analytics Tool

A powerful backend service that simulates a Gen AI Analytics data query system, enabling natural language processing of business queries.

## Features

- Natural language query processing
- Mock database simulation
- JWT-based authentication
- Query explanation and validation
- RESTful API endpoints

## Tech Stack

- Python 3.8+
- FastAPI
- SQLite (for development)
- JWT Authentication
- Pydantic for data validation

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd gen-ai-analytics
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

### Authentication

All endpoints require JWT authentication. Include the token in the Authorization header:
```
Authorization: Bearer <your-token>
```

### Endpoints

#### 1. Process Query
```http
POST /api/v1/query
```

Request body:
```json
{
    "query": "Show me sales performance by region for Q1 2024"
}
```

Response:
```json
{
    "query_id": "uuid",
    "results": [...],
    "execution_time": 0.123,
    "status": "success"
}
```

#### 2. Explain Query
```http
GET /api/v1/explain
```

Query parameters:
- `query_id`: UUID of the query to explain

Response:
```json
{
    "query_id": "uuid",
    "natural_language": "Show me sales performance by region for Q1 2024",
    "translated_query": "SELECT * FROM sales WHERE quarter = 'Q1' AND year = 2024",
    "execution_plan": {...},
    "estimated_cost": 0.5
}
```

#### 3. Validate Query
```http
POST /api/v1/validate
```

Request body:
```json
{
    "query": "Show me sales performance by region for Q1 2024"
}
```

Response:
```json
{
    "is_valid": true,
    "message": "Query is valid and can be processed",
    "suggestions": [...],
    "complexity_score": 0.7
}
```

## Testing with cURL

### 1. Process Query
```bash
curl -X POST "http://localhost:8000/api/v1/query" \
     -H "Authorization: Bearer <your-token>" \
     -H "Content-Type: application/json" \
     -d '{"query": "Show me sales performance by region for Q1 2024"}'
```

### 2. Explain Query
```bash
curl -X GET "http://localhost:8000/api/v1/explain?query_id=<query-id>" \
     -H "Authorization: Bearer <your-token>"
```

### 3. Validate Query
```bash
curl -X POST "http://localhost:8000/api/v1/validate" \
     -H "Authorization: Bearer <your-token>" \
     -H "Content-Type: application/json" \
     -d '{"query": "Show me sales performance by region for Q1 2024"}'
```

## Postman Collection

```json
{
    "info": {
        "name": "Gen AI Analytics API",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": [
        {
            "name": "Process Query",
            "request": {
                "method": "POST",
                "header": [
                    {
                        "key": "Authorization",
                        "value": "Bearer <your-token>",
                        "type": "text"
                    },
                    {
                        "key": "Content-Type",
                        "value": "application/json",
                        "type": "text"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": "{\"query\": \"Show me sales performance by region for Q1 2024\"}"
                },
                "url": {
                    "raw": "http://localhost:8000/api/v1/query",
                    "protocol": "http",
                    "host": ["localhost"],
                    "port": "8000",
                    "path": ["api", "v1", "query"]
                }
            }
        },
        {
            "name": "Explain Query",
            "request": {
                "method": "GET",
                "header": [
                    {
                        "key": "Authorization",
                        "value": "Bearer <your-token>",
                        "type": "text"
                    }
                ],
                "url": {
                    "raw": "http://localhost:8000/api/v1/explain?query_id=<query-id>",
                    "protocol": "http",
                    "host": ["localhost"],
                    "port": "8000",
                    "path": ["api", "v1", "explain"],
                    "query": [
                        {
                            "key": "query_id",
                            "value": "<query-id>"
                        }
                    ]
                }
            }
        },
        {
            "name": "Validate Query",
            "request": {
                "method": "POST",
                "header": [
                    {
                        "key": "Authorization",
                        "value": "Bearer <your-token>",
                        "type": "text"
                    },
                    {
                        "key": "Content-Type",
                        "value": "application/json",
                        "type": "text"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": "{\"query\": \"Show me sales performance by region for Q1 2024\"}"
                },
                "url": {
                    "raw": "http://localhost:8000/api/v1/validate",
                    "protocol": "http",
                    "host": ["localhost"],
                    "port": "8000",
                    "path": ["api", "v1", "validate"]
                }
            }
        }
    ]
}
```

## Deployment

### Railway Deployment

1. Create a Railway account and install the Railway CLI
2. Login to Railway:
```bash
railway login
```

3. Initialize Railway project:
```bash
railway init
```

4. Deploy the application:
```bash
railway up
```

### Render Deployment

1. Create a Render account
2. Connect your GitHub repository
3. Create a new Web Service
4. Configure the service:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Environment Variables: Copy from `.env.example`

### Heroku Deployment

1. Create a Heroku account and install the Heroku CLI
2. Login to Heroku:
```bash
heroku login
```

3. Create a new Heroku app:
```bash
heroku create gen-ai-analytics
```

4. Deploy the application:
```bash
git push heroku main
```

## Development

### Project Structure
```
gen_ai_analytics/
├── app/
│   ├── api/
│   │   ├── endpoints/
│   │   └── router.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── models/
│   │   └── query.py
│   ├── services/
│   │   ├── query_processor.py
│   │   ├── nlu_engine.py
│   │   └── mock_db.py
│   └── main.py
├── tests/
├── requirements.txt
└── README.md
```

### Running Tests
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 