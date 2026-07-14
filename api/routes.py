"""
API Health Check Module

This module provides a health monitoring endpoint for the FastAPI application.

Purpose:
    - Verify that the API server is active.
    - Allow external services or monitoring tools to check system availability.

Endpoint:
    GET /health

Response:
    {
        "status": "running"
    }

Role in System:

    Dashboard / External Service
              |
              ↓
          FastAPI API
              |
              ↓
        Health Router
"""

from fastapi import APIRouter


# Create API router for health-related endpoints
router = APIRouter()


@router.get("/health")
def health():
    """
    Check API server status.

    This endpoint is used as a lightweight health check
    to confirm that the FastAPI backend is operational.

    Returns:
        dict:
            API status information.

    Example Response:
        {
            "status": "running"
        }
    """

    return {
        "status": "running"
    }