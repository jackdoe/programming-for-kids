## [DAY-143] Strings

Print the characters of a string one by one:

```
a = 'hello'
for i in a:
    print(i)
```

Print the characters and their index:

```
a = 'hello'
for i in range(0,len(a)):
    print(i, a[i])
```

Reverse the characters:

```
a = 'hey'
rev = ''
for i in range(0,len(a)):
    # i = 0
    # a[2 - 0] -> a[2] -> y
    # i = 1
    # a[2 - 1] -> a[1] -> e
    # i = 2
    # a[2 - 2] -> a[0] -> h
    print(i,a[len(a)-1-i])
    rev +=a[len(a)-1-i]
print(rev)
```

Google 'how to reverse a string in python'

```
a = 'hello'
b = a[len(a)::-1]
print(b)
```

check out the stackoverflow explanation at https://stackoverflow.com/questions/509211


Answer by Greg Hewgill, https://stackoverflow.com/users/893/greg-hewgill
```

It's pretty simple really:

a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
There is also the step value, which can be used with any of the above:

a[start:stop:step] # start through not past stop, by step
The key point to remember is that the :stop value represents the first value that
 is not in the selected slice. So, the difference between stop and start is the 
 number of elements selected (if step is 1, the default).

The other feature is that start or stop may be a negative number, which means it 
counts from the end of the array instead of the beginning. So:

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
Similarly, step may be a negative number:

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed

Python is kind to the programmer if there are fewer items than you ask for. For example, 
if you ask for a[:-2] and a only contains one element, you get an empty list instead of 
an error. Sometimes you would prefer the error, so you have to be aware that this may happen.

Relation to slice() object
The slicing operator [] is actually being used in the above code with a slice() object 
using the : notation (which is only valid within []), i.e.:

a[start:stop:step]
is equivalent to:

a[slice(start, stop, step)]

Slice objects also behave slightly differently depending on the number of arguments, 
similarly to range(), i.e. both slice(stop) and slice(start, stop[, step]) are 
supported. To skip specifying a given argument, one might use None, so that e.g. 
a[start:] is equivalent to a[slice(start, None)] or a[::-1] is equivalent to 
a[slice(None, None, -1)].

While the :-based notation is very helpful for simple slicing, the explicit use of 
slice() objects simplifies the programmatic generation of slicing.
```

## [DAY-143] Strings; Lists

Sum the ascii of the elements of a list.

```
a = ['h','e','l','l','o']
sum = 0
for i in a:
    sum += ord(a)

print(sum)
```

Print its index, and the letter with the corresponding ascii


```
a = ['h','e','l','l','o']
sum = 0
for i in range(len(a)):
    m = ord(a[i])
    print('index: ', i, a[i], '=', m)
    sum += m

print(sum)
```

Now do the same with a string

```
a = 'hello'
sum = 0
for i in range(len(a)):
    m = ord(a[i])
    print('index: ', i, a[i], '=', m)
    sum += m

print(sum)
```

See how lists and strings both have len() and are indexable, meaning you can go to a specific index a[i] and do something.

You can mutate (change) the list, meaning you can change its content
```
a = ['h','e','l','o']
a[2] = 'b'
print(a)
```

But you can not change a string inplace:
```
a = 'hello'
a[2] = 'b'
print(a)
```

You will get `TypeError: 'str' object does not support item assignment`. If you want to change a string, you have to make a new one and reasign the variable to point to the new string.

```
a = 'hello'

a = a[0:2] + 'b' + a[3:5]
```

See how we make completely new string, made up from the parts of the old string, and also the letter 'b' in the middle, and we make the variable `a` point to the new string.



