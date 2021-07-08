echo > README.md
for i in  cover.md hello.md $(ls -1 week-*.md | sort -n); do
    cat $i >> README.md
    echo >> README.md
done