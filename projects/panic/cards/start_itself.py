import os

print("PANIC")

# __file__ is the name of the current
# python script, if you save this card
# as "hello.py", in the directory
# /a/b/c/ then __file__ will be
# /a/b/c/hello.py
#
# so this program will just start itself
# and then start itself, and then start
# itself...
os.system(f"python {__file__}")

