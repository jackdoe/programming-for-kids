# for each number from 1 to 20
#   if divisable by 3 and 5
#     print fizzbuzz
#   if something is divisable by 3
#     print fizz
#   if something is divisable by 5
#     print buzz
#   else
#     print the integer
def fizzbuzz():
  fb = []
  for i in range(1,21):
    if i % 3 == 0 and i % 5 == 0:
      fb.append("fizzbuzz")
    elif i % 3 == 0:
      fb.append("fizz")
    elif i % 5 == 0:
      fb.append("buzz")
    else:
      fb.append(i)

  return fb

fizzy = fizzbuzz()
print(fizzy[⚂ - 1])
