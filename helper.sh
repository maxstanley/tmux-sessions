#!/bin/bash

session=$(python3 ./start.py)
tmux new -s $session

