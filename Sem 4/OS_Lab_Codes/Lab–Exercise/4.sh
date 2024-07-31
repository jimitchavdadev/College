# 4) Write a user management script with options to add a new user, remove an
# existing user, and list all users on the system.

#!/bin/bash

# Function to add a new user
add_user() {
    echo "Enter username to add: "
    read username
    sudo adduser $username
}

# Function to remove an existing user
remove_user() {
    echo "Enter username to remove: "
    read username
    sudo deluser $username
}

# Function to list all users
list_users() {
    cut -d: -f1 /etc/passwd
}

# Main script
echo "User Management Script"
echo "1. Add a new user"
echo "2. Remove an existing user"
echo "3. List all users"
read choice

case $choice in
    1) add_user ;;
    2) remove_user ;;
    3) list_users ;;
    *) echo "Invalid option" ;;
esac
