#!/bin/bash

echo "Enter three numbers:"

read -p "Enter number 1: " num1
read -p "Enter number 2: " num2
read -p "Enter number 3: " num3

largest=$num1

if [ $num2 -gt $largest ]; then
    largest=$num2
fi

if [ $num3 -gt $largest ]; then
    largest=$num3
fi

echo "The largest number is: $largest"
