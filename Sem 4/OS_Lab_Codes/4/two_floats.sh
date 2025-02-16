#!/bin/bash
echo "Enter the two float numbers to be added:"
read num1
read num2
sum=$(echo "$num1 + $num2" | bc)
echo "The sum is: $sum"
