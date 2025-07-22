#!/bin/bash

# Initial base64-encoded string
data="Vm0wd2QyVkZOVWRpUm1ScFVtMW9WRmx0ZEhkVU1WcDBUVmM1VjFKdGVGWlZNakExVmpGYWRHVkVRbUZXVmxsM1ZtcEJlRmRIVmtsalJtaG9UV3N3ZUZadGRGWmxSbGw0V2toR1VtSlZXbGhXYlhoelRURmFjbFZyWkZwV01VcElWbTAxVjJGc1NuUmhSemxWVm0xb1JGbHFSbHBsUm1SelYyMTRVMkpJUWpWV1IzaGhXVmRHVjFOdVRsaGhlbXhZV1d4b1UwMHhWWGhYYlhSWFRWaENTbGt3WkRSVk1ERkZVbFJDVjJGcmEzaFZla3BMVWpGT2RWUnNhR2xTTW1oWFZtMTBWMU14VWtkalJscFlZbGhTY1ZsclpGTmxiRmw1WTNwR1YwMVdjRWhXTW5CaFZqSkZlVlZVUWxkaGExcG9WVEJhUzJOV1pITmFSMnhvWld4YWIxWXhaREJaVmxwMFZWaG9hbEp0YUhOVmFrSmhWa1phZEdSSVpHeGlSbkJKV2xWa1IyRkdTWGhYYm5CWFRXNVNkbFpxUmt0U2JHUnpZVVprYUdFeGNHOVdWM0JIWkRGS2RGTnJaRlJpVjNoVVZteG9RMlJzV25STldHUlZUV3RzTlZadGVHdGhiRXBYVjJ4U1dtRXhWWGhXYTFwelkyeGtjbVJIZUZkaVJsa3hWMVJPZDFZeFduSk5WbVJxVWxkb1dGUlhOVzloUmxweFVtdHdiR0pHV2pGV01qRkhWVEZLVjJOR1VsaGlSbkJvVlhwS1UxWXhWblZVYkZacFZqSm9kMVpYZUc5Uk1XUkhWMjVLV0dKSFVtRldiWE40VGtaV2MyRkhPVmRpVlhCNVZHeGFiMVl5UlhoWGJXaFhWbFp3ZWxreWVHRldWa3B6V2tkc1UySkhPVE5XTVZKUFpERlplRmRZWkU1V2JIQnhWVzB4VTFkR2JITmhSVTVYVW14d01GcFZaRWRWTWtwV1RsVndWbUpZYUZoV1IzaGhaRlpHY2xac1pHbFNNVVYzVmxaU1IxbFdXbkpOVmxwWFlYcFdWRlZyVmtaT1VUMDk="

iteration=0

while true; do
    iteration=$((iteration + 1))
    echo "Iteration $iteration: Decoding..."
    
    # Try decoding
    decoded=$(echo "$data" | base64 -d 2>/dev/null)

    # Check if decoding failed
    if [ $? -ne 0 ]; then
        echo "Decoding failed. Exiting."
        break
    fi

    # Check for meaningful output (heuristic: does it contain at least 5 printable ASCII words?)
    printable_words=$(echo "$decoded" | grep -Eo '[[:print:]]+' | wc -l)
    
    echo "$decoded"

    if [ $printable_words -ge 5 ]; then
        echo "🟢 Found possibly meaningful content after $iteration iterations!"
        break
    fi

    # Prepare for next round
    data="$decoded"

    # Wait 1 second
    sleep 1
done
