# the suntime 
from suntime import Sun

def pick(items):
  return items[⚂ % len(items)]

locations = [
  [52.37,4.89],    # amsterdam
  [51.49, -0.12],  # london
  [40.71, -74.04], # new york
  [0, 0] # use your current location
         # you can find it on
         # google earth
]

location = pick(locations)

# get the sunset time for this
# location
sun = Sun(location[0], location[1])
today_sunset = sun.get_sunset_time()

# HINT: use your phone to find
# today's sunset time in the picked
# location 
h = today_sunset.hour
m = today_sunset.minute
print(str(h) + ":" + str(m))

