# `import` loads a module, a module
# is a just a bunch of code you are
# adding to your program because it
# helps you to solve a problem,
# e.g. the datetime module gives you
# functionality to get the current
# date and time. You can also
# download modules for python using
# the `pip3` command. Some modules
# are coming directly with python,
# like `random` and `datetime`.
import datetime

# now() returns an object that has:
#  now.year
#  now.month
#  now.day
#  now.hour
#  now.minute
#  now.second
now = datetime.datetime.now()

meeting_time = ⚂

# check your watch, if the current
# minute is less than the
# meeting_time then you are on time!
if now.minute < meeting_time:
  print('on time')
else:
  print('you are late')
