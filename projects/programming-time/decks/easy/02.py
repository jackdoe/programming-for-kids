# a dictionary is a way to lookup
# keys and values in this example we
# have the Care Bear name as key
# and its color as value
bears = {
  "Bedtime Bear": "Aqua blue",
  "Birthday Bear": "Golden yellow",
  "Cheer Bear": "Carnation pink",
  "Friend Bear": "Peach",
  "Funshine Bear": "Lemon yellow",
  "Good Luck Bear": "Green",
  "Grumpy Bear": "Indigo blue",
  "Love-A-Lot Bear": "Magenta pink",
  "Tenderheart Bear": "Brown",
}

favorite = [
  "Cheer Bear",
  "Love-A-Lot Bear",
  "Friend Bear"
]

# Pick a random bear from the list
# of favorite names
you = favorite[⚂ % len(favorite)]

# for example bears["Grumpy Bear"]
# is "Indigo Blue"
color = bears[you]
print('your color: ' + color)
