#!/bin/bash

PARENT_COMMAND=$(dirname $0)

session=$(python3 $PARENT_COMMAND/start.py)
tmux new -s $session

