#!/bin/bash

echo "Enter the value of n:"
read n

# Initialize the first two Fibonacci numbers
a=0
b=1

echo "First $n Fibonacci numbers:"

for ((i = 1; i <= n; i++)); do
    echo -n "$a "

    # Calculate the next Fibonacci number
    next=$((a + b))

    # Update values for the next iteration
    a=$b
    b=$next

done
echo " "
