# 6) Write a bash script that utilizes system calls to create a directory and a file
# within that directory.

#!/bin/bash

# Function to create directory and file
create_dir_and_file() {
    echo "Enter directory name: "
    read directory
    mkdir $directory
    echo "Enter file name: "
    read filename
    touch "$directory/$filename"
    echo "Directory '$directory' and file '$filename' created successfully."
}

# Main script
create_dir_and_file
