class HandmadeRange:
  def __init__(self,start,end,skip):
    self.start = start
    self.end = end
    self.skip = skip

  def __iter__(self):
    self.n = self.start
    return self

  def __next__(self):
    if self.n < self.end:
      result = self.n
      self.n += self.skip
      return result
    else:
      # Raise an exception when we
      # reach the end. An exception
      # is a way to communicate
      # between multiple function
      # calls. For example dividing
      # by zero throws ZeroDivision:
      #   a = 1
      #   try:
      #      print(a/0)
      #   except ZeroDivisionError:
      #      print("0 is illegal")
      raise StopIteration

for i in HandmadeRange(0,25,⚂):
  print(i)
