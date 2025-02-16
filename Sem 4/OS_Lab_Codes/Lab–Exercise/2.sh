# 2) Write a bash script that monitors and displays the current CPU and memory
# usage of the system.

#!/bin/bash

# Function to display CPU and memory usage
monitor_usage() {
    echo "CPU Usage:"
    top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}'
    echo "Memory Usage:"
    free -m | awk 'NR==2{printf "Total: %s MB\nUsed: %s MB\nFree: %s MB\n", $2,$3,$4}'
}

# Main script
monitor_usage
