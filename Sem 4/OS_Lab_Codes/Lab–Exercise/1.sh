# 1) Write a bash script to add 2 float numbers

#!/bin/bash

# Function to add two float numbers
add_float() {
    local result=$(echo "$1 + $2" | bc -l)
    echo $result
}

# Main script
echo "Enter first float number: "
read num1

echo "Enter second float number: "
read num2

result=$(add_float $num1 $num2)
echo "The sum is: $result"
