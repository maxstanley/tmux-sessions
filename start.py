#!/usr/bin/env python3
import subprocess

# List of available tmux sessions to use.
available_sessions = [
    "0PRIMARY",
    "1SECONDARY",
    "2TERTIARY",
    "3QUATERNARY"
]

# Get the list of the currently running tmux clients.
tmux_sessions = subprocess.run(
    ["tmux", "list-clients"],
    capture_output=True
)

# Get the list of the currently running tmux sessions.
tmux_sessions = tmux_sessions.stdout.decode("utf-8").split("\n")[:-1]
tmux_sessions = [s.split(' ')[1] for s in tmux_sessions]

# Subtract the available_sessions from the running tmux sessions.
available_sessions = list(set(available_sessions) - set(tmux_sessions))
available_sessions.sort()

# Return the first available sessions from the list of available_sessions.
print(available_sessions[0])

