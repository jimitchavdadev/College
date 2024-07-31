# 3) Write a bash script that takes a user-input file and destination directory,
# then creates a backup of the file in the specified destination

#!/bin/bash

# Function to create a backup of a file
backup_file() {
    cp "$1" "$2"
    echo "Backup created successfully."
}

# Main script
echo "Enter the file to backup: "
read file

echo "Enter the destination directory: "
read destination

backup_file $file $destination
