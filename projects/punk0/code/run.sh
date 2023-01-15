#!/bin/sh


set -e

for kind in draw increment reset reverse rotate shift sort_asc sort_desc; do
    echo
    echo $kind
    echo '> go'
    :> /tmp/a
    go run $kind.go | paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
    echo '> js'
    node $kind.js| paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
    echo '> py'
    python3 $kind.py| paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
    echo '> c'

    if [ $kind = "draw" ]; then
        gcc -Wall -Wextra -o /tmp/z draw1.c >/dev/null
        /tmp/z | paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
        gcc -Wall -Wextra -o /tmp/z draw2.c >/dev/null
        /tmp/z | paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
        gcc -Wall -Wextra -o /tmp/z draw3.c >/dev/null
        /tmp/z | paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a

        python3 draw1.py| paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
        python3 draw2.py| paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
        python3 draw3.py| paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
        node draw1.js| paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
        node draw2.js| paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
        node draw3.js| paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
        go run draw1.go | paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
        go run draw2.go | paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
        go run draw3.go | paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
    fi

    if [ $kind = "shift" ]; then
        gcc -Wall -Wextra -o /tmp/z shift1.c >/dev/null
        /tmp/z | paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
        go run shift1.go | paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
        node shift1.js| paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
        python3 shift1.py| paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a
    fi
    
    
    gcc -Wall -Wextra -o /tmp/z $kind.c >/dev/null
    /tmp/z | paste -sd ' ' - | sed -e 's/, /,/g' | sed -e 's/ /,/g' >> /tmp/a

    echo 'counted uniq:'
    cat /tmp/a

    lines=$(cat /tmp/a | sort | uniq -c | wc -l)
    if [ "$lines" -ne "1" ]; then
        echo "NOOO"
        exit 1
    fi
done
                
