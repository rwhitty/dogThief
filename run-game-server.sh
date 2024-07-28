#!/bin/bash

PID=$(lsof -t -i:5000)

if [ -n "$PID" ]; then
  kill $PID
fi

git pull origin main

python3 game/App.py