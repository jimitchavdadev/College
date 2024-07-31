#!/bin/bash
echo "Enter the first number: "
read num1
echo "Enter the second number: "
read num2
echo "Enter the third number: "
read num3

largest=$num1

if [ $num2 -gt $largest ]; then
    largest=$num2
fi

if [ $num3 -gt $largest ]; then
    largest=$num3
fi

echo "The largest number is: $largest"

sum=$((num1 + num2 + num3))
mean=$(echo "scale=2; $sum / 3" | bc)

echo "The sum of the numbers is: $sum"
echo "The mean of the numbers is: $mean"
