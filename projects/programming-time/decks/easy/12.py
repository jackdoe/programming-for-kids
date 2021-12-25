# use the fullmoon module to
# compute when the next full moon is
from fullmoon import NextFullMoon
import datetime

# NextFullMoon() returns an object
# which has next_full_moon() method,
# which returns datetime object of
# the next full moon
n = NextFullMoon().next_full_moon()

# datetime.now() returns the current
# datetime
today = datetime.datetime.now()

# You can subtract datetime objects
# from eachother, it returns a date
# difference object which has .days
# property to get the difference in
# days. Since `n` is in the future,
# subtracting `today` from it will
# return the days remaining to the
# next full nmoon.
diff = n - today
remaining = diff.days

# HINT: use your phone to lookup
# when the next full moon is and
# count the days from now to compute
# the result of this card.
print(remaining)
