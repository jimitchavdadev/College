#!/bin/bash
echo "Menu-driven Calculator"
echo "1. Addition"
echo "2. Subtraction"
echo "3. Multiplication"
echo "4. Division"
echo -n "Enter your choice: "
read choice
echo -n "Enter the first number: "
read num1
echo -n "Enter the second number: "
read num2
case $choice in
1) result=$(echo "$num1 + $num2" | bc) ;;
2) result=$(echo "$num1 - $num2" | bc) ;;
3) result=$(echo "$num1 * $num2" | bc) ;;
4) result=$(echo "scale=2; $num1 / $num2" | bc) ;;
*) echo "Invalid choice" ;;
esac
echo "Result: $result"
