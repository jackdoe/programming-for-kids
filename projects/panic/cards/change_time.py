# pip install win32api
import win32api,datetime,time, random

# set the time to be:
# current time + n minutes
def bump(n):
  d = datetime.datetime.now()
  minute = d.minute
  if minute < 60-n:
    minute += n
  # else we have to bump the hour, and
  # if hour is close to midnight, bump
  # the day, and the month and etc..  so
  # up to minute 60-n is good enough
  win32api.SetSystemTime(
    d.year,
    d.month,
    d.weekday(),
    d.day,
    d.hour,
    minute,
    d.second,
    0)

while True:
  # sleep between 10 and 20 minutes
  time.sleep(600,1200)

  # bump between 1 and 5 minutes
  bump(random.randint(1,5))
