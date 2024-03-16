cat cover.md hello.md > book.md
for i in $(ls -1 weeks/week-*.md | sort -k 2 -t- -n); do
    cat $i >> book.md
    echo >> book.md
done

