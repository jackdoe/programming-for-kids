# RSA - algorithm is possibly the
# most used encryption algorithm in
# the world.
# in our example we use small prime
# numbers, but 3564925531837 and
# 754875236820775169247373371859 are
# also prime numbers

p = 11 # must be prime number
q = 17 # must be prime number
e = 7 # prime number between
      # (p-q)*(q-1), in our case
      # (11-1)*(17-1) = 160
      # so `e` must be a prime
      # number > 1 and < 160,
      # so I picked 7 as its also
      # my lucky number.
N = p * q # 187

message = ⚂

# 2**5 is 2*2*2*2*2 = 32
encrypted = (message**e) % N
print(encrypted)

# // is floor division:
# x//y is the same as int(x/y)
# e.g. 5/2 is 2.5, but 5//2 is 2
d = (((p-1) * (q-1)) + 1) // e
decrypted = (encrypted**d) % N
print(decrypted)
