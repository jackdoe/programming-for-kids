import os
import random

possible = ["a b c", "hello","world", "has space","maybe empty","empty","not empty"]

def md(p):
    one_of_five = ''
    for i in range(1,6):
        a = random.choice(possible)
        one_of_five= a
        os.makedirs(os.path.join(p,a), exist_ok=True)

    return one_of_five


p = os.path.join(".","secret mission")
for i in range(10):
    p = os.path.join(p, md(p))
    print(p)

with open(os.path.join(p, "password.txt"), "w") as f:
    f.write("the password is: " + str(477217972* 31))
