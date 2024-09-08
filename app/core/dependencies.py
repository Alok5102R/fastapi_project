# app/core/dependencies.py
from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-KEY")

def validate_api_key(api_key: str = Depends(api_key_header)):
    if api_key != "expected_key":
        raise HTTPException(status_code=403, detail="Invalid API Key")