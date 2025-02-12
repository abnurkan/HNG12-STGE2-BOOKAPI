#!/bin/bash
# Start Nginx in the background
nginx -g "daemon off;" &

# Start FastAPI using Gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
