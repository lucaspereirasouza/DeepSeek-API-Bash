#!/bin/bash

VENV_DIR="venv"

function check_venv() {
    if [ -d "$VENV_DIR" ]; then
        echo "Ambiente virtual encontrado em $VENV_DIR."
        return 0
    else
        echo "Ambiente virtual não encontrado. Criando um novo..."
        return 1
    fi
}

function setup_venv() {
    python3 -m venv $VENV_DIR
    source $VENV_DIR/bin/activate
    pip install --upgrade pip
    pip install flask python-dotenv
}

if ! check_venv; then
    setup_venv
fi

source $VENV_DIR/bin/activate


./run.sh