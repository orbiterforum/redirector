#!/bin/sh
set -e

exec uvicorn redirector.main:app --host 0.0.0.0 --use-colors --port 8000