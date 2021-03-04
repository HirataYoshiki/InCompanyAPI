#!/bin/bash

cd /tmp/dev/backend
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
