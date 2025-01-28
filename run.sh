#!/bin/bash

DIR=$(dirname "$0")
PY_= "$DIR" ""./venv/bin/python"

echo "Iniciando o servidor Flask..."

PY_ main.py &

FLASK_PID=$!

echo "Iniciando o cliente de terminal..."
PY_ terminalUI.py

echo "Encerrando o servidor Flask..."
kill $FLASK_PID

deactivate