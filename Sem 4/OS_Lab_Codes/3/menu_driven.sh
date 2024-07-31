#!/bin/bash

echo "Main Menu"
echo "1. Display calendar of current month"
echo "2. Display today’s date information"
echo "3. Display the username of the users currently logged in"
echo "4. Display the username at given coordinates"
echo "5. Display the terminal number"
echo "6. Exit"
echo -n "Enter your choice: "
read choice
case $choice in
1) cal ;;
2) date ;;
3) who ;;
4)
    read -p "Enter X position: " x
    read -p "Enter Y position: " y
    tput cup $x $y
    echo -n $USER
    ;;
5) tty ;;
6) exit ;;
*) echo "Invalid choice" ;;
esac
