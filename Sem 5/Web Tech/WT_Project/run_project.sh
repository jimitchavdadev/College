#!/bin/bash

# Define your project directory and the Apache document root directory
PROJECT_DIR=~/Roger/College/Sem\ 5/Web\ Tech/WT_Project
APACHE_DIR="/var/www/html/election_project"

# Check if Apache and MySQL are installed, start them if not already running
echo "Starting Apache and MySQL..."

# Start Apache and MySQL if they aren't already running
sudo systemctl start apache2
sudo systemctl start mysql

# Enable Apache and MySQL to start on boot (optional)
sudo systemctl enable apache2
sudo systemctl enable mysql

# Check if the Apache directory exists, if not create it
if [ ! -d "$APACHE_DIR" ]; then
    echo "Creating directory for the project at $APACHE_DIR..."
    sudo mkdir -p $APACHE_DIR
fi

# Copy your project files to Apache's root directory
echo "Copying project files to Apache's web directory..."
sudo cp -r $PROJECT_DIR/* $APACHE_DIR/

# Set the correct file permissions
echo "Setting file permissions..."
sudo chown -R $USER:$USER $APACHE_DIR
sudo chmod -R 755 $APACHE_DIR

# Restart Apache to make sure all changes take effect
echo "Restarting Apache..."
sudo systemctl restart apache2

# Open the project in the browser
echo "Opening the project in the browser..."
xdg-open "http://localhost/election_project/register.html"

