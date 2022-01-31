# Diffie–Hellman Key Exchange
# algorithm is a method to compute a
# shared secret over public channel
p = 23    # publicly shared prime
g = 5     # publicly shared base

a = ⚂     # Alice's private secret
b = ⚂     # Bob's private secret

A = (g**a) % p
# Alice yells `A` to Bob
# anyone can hear it!
print("Alice -> Bob: ", A)

B = (g**b) % p
# Bob yells `B` to Alice
# anyone can hear it!
print("Bob -> Alice: ", B)

# Alice Computes shared secret based
# on B (yelled publicly by Bob), her
# secret `a` and the shared prime
# number `p`
ab = (B**a) % p

# Bob does the same, but with his
# secret `b`, and the value `A` he
# heard from Alice
ba = (A**b) % p

print("Shared Secret:", ab, ba)
