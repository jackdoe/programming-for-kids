# * swap the rating and title column

paste -d, <(cat 03.txt | cut -f 2 -d,) <(cat 03.txt | cut -f 1 -d,) <(cat 03.txt | cut -f 3 -d,) <(cat 03.txt | cut -f 4 -d,) <(cat 03.txt | cut -f 5 -d,)

# * print the last row's votes

cat 03.txt | tr "," "\n" | tail -1 
cat 03.txt | cut -f 5 -d, | tail -1

# * remove the Rank and Votes column

paste -d, <(cat 03.txt | cut -f 2 -d ',') <(cat 03.txt | cut -f 3 -d ',') <(cat 03.txt | cut -f 4 -d ',') 
cat 03.txt | cut -f 2,3,4 -d,

# * print only the title column capitalized

cat 03.txt | cut -f 2 -d, | tr "[a-z]" "[A-Z]"

# * print the first and the last row

cat <(cat 03.txt | head -2 | tail -1) <(cat 03.txt | tail -1)


# * print the votes difference between
#  the top and bottom voted movie

paste -d- <(cat 03.txt | grep -v Rank | cut -f 5 -d, | sort -n | tail -1) <(cat 03.txt | grep -v Rank | cut -f 5 -d, | sort -n | head -1) | bc

# * sum the votes

cat 03.txt  | cut -f 5 -d, | grep -v Votes | paste -sd+ | bc
paste -sd+ <(cat 03.txt  | cut -f 5 -d, | grep -v Votes) | bc

# * sum the votes of movies in 2016
paste -sd+ <(cat 03.txt | grep 2016 | cut -f 4 -d, | grep -v Rating)  | bc 
cat 03.txt | grep 2016 | cut -f 4 -d, | grep -v Rating | paste -sd+ | bc 

#* show the best ranked title 
#  (only title, no other columns)
paste -d, <(cat 03.txt | cut -f 4 -d,) <(cat 03.txt | cut -f 2 -d,)  | grep -v Rating | sort -n | tail -1 | cut -f2 -d,


# * replace commas with tabs
cat 03.txt | tr "," "\t"

# * print the titles but as a giant
#  string Sing Interstellar ...
cat 03.txt | cut -f 2 -d, | tr "\n" " "
cat 03.txt | cut -f 2 -d, | paste -sd' '

# remove the spaces, commas and digits (removed too easy)
cat 03.txt | tr -d ' ,' | tr -d '[:digit:]'

# (REMOVED: too much) 
# * uppercase the titles but not
#  the header
cat <(cat 03.txt| head -1) <(paste -d, <(cat 03.txt | tail -30 | tr "[a-z]" "[A-Z]"))



# compute average rating
paste -d/- <(cat 03.txt  | cut -f 4 -d, |grep -v Rating| paste -sd+ | bc) <(cat 03.txt  | grep -v Rating | wc -l) | bc
