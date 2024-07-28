#!/bin/bash

PID=$(lsof -t -i:5000)

if [ -n "$PID" ]; then
  kill $PID
fi

python3 game/App.py