#!/bin/bash
uvicorn app:create_app --workers 1 --host 0.0.0.0 --port 8080 --factory
