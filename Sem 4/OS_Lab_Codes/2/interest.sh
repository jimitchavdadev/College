echo "Enter the principle amount:"
read pamount
echo "Enter the interest rate:"
read interest
echo "Enter the number of years:"
read years 
net_interest=$((pamount * interest * years / 100))
echo "total return value is $net_interest"
