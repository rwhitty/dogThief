#!/bin/bash

PID=$(lsof -t -i:5000)

if [ -n "$PID" ]; then
  kill $PID
fi

git pull origin main

python3 /home/ec2-user/projects/dogthief/game/App.py