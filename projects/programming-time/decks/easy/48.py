# Files are just collection of bytes
# that are stored on disk. You can
# find them by their name. The
# computer uses a special
# data-structure, called a
# filesystem, to allow you to access
# your files quickly.  Each file has
# some attributes attached to it,
# like its size who can access it,
# who created it, when it was
# created, or modified.

# To open a file use the built-in
# function open() with parameters of
# the filename and parameter to
# specify if you want to read(r) or
# write(w)

file = open("hello.txt","w")
file.write("hi") # [a][a]
file.close()

file = open("hello.txt","r")
data = file.read()
file.close()

print(data)
