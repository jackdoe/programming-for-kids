echo > book.md
echo > README.md
python3 toc.py
for i in  cover.md hello.md toc.md $(ls -1 week-*.md | sort -k 2 -t- -n); do
    cat $i >> book.md
    echo >> book.md
done

cat cover.md hello.md toc.md frontpage.md > README.md

python3 extract.py
