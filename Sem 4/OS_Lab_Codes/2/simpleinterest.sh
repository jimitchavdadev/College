echo "enter the principle amount:"
read pamount
echo "enter interest rate:"
read interest
echo "enter number of years:"
read years
total=$((pamount * interest * (years) / 100))
echo "total return value is $total"
