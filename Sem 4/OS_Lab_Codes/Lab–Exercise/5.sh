# 5) Write a script that retrieves and displays information about the network,
# including the hostname, IP address, and a list of network interfaces.

#!/bin/bash

# Function to retrieve network information
network_info() {
    echo "Hostname:"
    hostname
    echo "IP Address:"
    ip addr show | awk '/inet /{print $2}'
    echo "Network Interfaces:"
    ip link show | awk -F': ' '$0 !~ "lo|vir|^[^0-9]"{print $2}'
}

# Main script
network_info
