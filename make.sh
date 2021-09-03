echo > README.md
for i in  cover.md hello.md $(ls -1 week-*.md | sort -k 2 -t- -n); do
    cat $i >> README.md
    echo >> README.md
done

python3 extract.py