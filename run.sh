#!/bin/bash

DIR=$(dirname "$0")
PY_= "$DIR" ""./venv/bin/python"

echo "Starting Flask..."

PY_ main.py &

FLASK_PID=$!

echo "Starting Client..."
PY_ terminalUI.py

echo "Finishing Flask..."
kill $FLASK_PID

deactivate