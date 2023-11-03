# pip install pywin32
import win32api,time,random
# POSSIBLE ANTICHEAT TRIGGER
# set the time to be:
# current time + n minutes
def bump(n):
  d = time.gmtime()
  minute = d.tm_min
  if minute < 60-n:
    minute += n
  # else we have to bump the hour, and
  # if hour is close to midnight, bump
  # the day, and the month and etc..  so
  # up to minute 60-n is good enough

  win32api.SetSystemTime(
    d.tm_year,
    d.tm_mon,
    d.tm_wday,
    d.tm_mday,
    d.tm_hour,
    minute,
    d.tm_sec,
    0)

while True:
  # bump between 1 and 5 minutes
  bump(random.randint(1,5))

  time.sleep(600)
