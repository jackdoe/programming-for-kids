## [DAY-367] functions

make a fizzbuzz function that takes a parameter the final number to fizzbuzz to, also make another function to check if a number is prime, and print the prime numbers in the fizzbuzz function


```
def is_prime(n):
    if n== 0 or n == 1:
        return False
    for x in range(2,n):
        if n %x==0:
             return False
    return True
def fizzz(x):    
    for i in range(x):
        if i%15==0:
            print("fizzbuzz")
        elif i%5==0:
            print("buzz")
        elif i%3==0:
            print("fizzz")
        else:
            if is_prime(i):
                print("prime " + str(i))
            else:
                print(i)
fizzz(100000000000000)

```
