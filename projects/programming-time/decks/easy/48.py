# Files are just collection of bytes
# that are stored on disk.  You can
# open them by their name.

# To open a file use the builtin
# function open() with parameters of
# the filename and parameter to
# specify if you want to read(r) or
# write(w)

file = open("hello.txt","w")
file.write("hi")
file.close()


file = open("hello.txt","r")
data = file.read()
file.close()

print(data)
