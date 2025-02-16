max=-999999
for i in $@; do
    if [ $i -gt $max ]; then
        max=$i
    fi
done
echo "maximum=$max"
