# Production Ready FastAPI

## Overview
A FastAPI application structured for production, featuring modular routing, Pydantic models, and more.

## Project Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `uvicorn app.main:app --reload`

## Features
- Modular routing
- Pydantic data validation
- JWT-based authentication
- Async database operations

## Environment Variables
Set up a `.env` file with the following variables:


## Project Directory:
- app/: Contains the main application code.
- api/: Contains API route definitions, organized by version (e.g., v1, v2).
- core/: Contains core settings, configurations, and security utilities.
- models/: Database models using an ORM like Peewee or SQLAlchemy.
- services/: Contains business logic and service classes.
- db/: Database connection and session management.
- tests/: Contains unit and integration tests.