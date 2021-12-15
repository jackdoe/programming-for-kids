# To see if something is contained
# in a list, we go over each element
# in the list, and see if its equal
# to the element we are looking for.
# Pretty similar to how you would
# find needle in a haystack. Or how
# you are searching for your flight
# on the airport dashboard, you
# start from the top, and look down
# to see if the flight name matches
# your ticket.
def contains(haystack, needle):
  for x in haystack:
    if x == needle:
      return True

  return False

# 0 Mon, 1 Tue, 2 Wed, 3 Thu, 4 Fri
# 5 Sat, 6 Sun
weekday = [0,1,2,3,4]
weekend = [5,6]
day = ⚂
# or just use 'if day in weekday' 
if contains(weekday, day):
  print('work work')
elif contains(weekend, day):
  print('yey, weekend')
else:
  print('oops, expected 0 to 6')

