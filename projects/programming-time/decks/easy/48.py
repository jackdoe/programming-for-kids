# Files are just collection of
# bytes that are stored on disk
# and you can open them by their
# name.

# to open a file use the builtin
# function open()
# with parameters of the filename
# and do you want to read(r) or
# write(w) in the file.

file = open("hello.txt","w")
file.write("hi")
file.close()


file = open("hello.txt","r")
data = file.read()
file.close()

print(data)
