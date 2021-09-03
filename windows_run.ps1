$env:FASTAPI_ENV = "development"
$env:API_URL = "http://127.0.0.1:8000"
uvicorn main:app --reload --port=4000