# The RSA algorithm is possibly the
# most used encryption algorithm in
# the world. In our example we use
# small prime numbers, but 3389 and
# 2178583086560517094530555255075673
# are also prime numbers. Usually
# RSA uses prime numbers with more
# than 300 digits (1024 bit numbers)
p = 11 # must be prime number
q = 17 # must be prime number
e = 7 # prime number between
      # (p-1)*(q-1), in our case
      # (11-1)*(17-1) = 160
      # so `e` must be a prime
      # number > 1 and < 160,
      # so I picked 7 as its also
      # my lucky number.
d = 23 # number such that:
       # φ(N) = (p-1)*(q-1)
       # (d * e) % φ(N) = 1
       # so: (23 * 7) % 160 = 1
N = p * q # 187, called modulus

message = 50 + ⚂

# 2**5 is 2*2*2*2*2 = 32
encrypted = (message**e) % N
print(encrypted) # e,N: public key

decrypted = (encrypted**d) % N
print(decrypted) # d,N: private key
