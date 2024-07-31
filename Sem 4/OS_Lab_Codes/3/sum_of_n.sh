#!/bin/bash

sum=0

echo "Enter the number of inputs (n):"
read n

echo "Enter $n numbers:"

for ((i = 1; i <= n; i++)); do
    echo -n "Enter number $i: "
    read num
    sum=$((sum + num))
done

echo "Sum of $n numbers is: $sum"
