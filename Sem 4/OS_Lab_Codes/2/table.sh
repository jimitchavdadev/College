echo "hello enter a number:"
read num
for ((i = 1; i < 11; i++)); do
    result=$((num * i))
    echo "$num * $i = $result"
done
