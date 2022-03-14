from Crypto.Util.number import getPrime, inverse, bytes_to_long, isPrime
from random import randrange, choices
from hashlib import sha1
import string


class DSA(object):
    def __init__(self, p, q, g, y, x, k):
        self.p = p
        self.q = q
        self.g = g
        self.y = y
        self.x = x
        self.k = k
        # while True:
        #     self.q = getPrime(160)
        #     r = randrange(1 << 159, 1 << 160)
        #     self.p = self.q * r + 1
        #     if isPrime(self.p) != True:
        #         continue
        #     self.g = pow(2, r, self.p)
        #     if self.g == 1:
        #         continue
        #     self.x = randrange(2, self.q)
        #     self.y = pow(self.g, self.x, self.p)
        #     self.k = inverse(self.x, self.q)
        #     break

    def sign(self, msg):
        r = pow(self.g, self.k, self.p) % self.q
        h = bytes_to_long(sha1(msg).digest())
        s = inverse(self.k, self.q) * (h + self.x * r) % self.q
        return (r, s)

    def verify(self, msg, sig):
        r, s = sig
        if s == 0:
            return False
        s_inv = inverse(s, self.q)
        h = bytes_to_long(sha1(msg).digest())
        e1 = h * s_inv % self.q
        e2 = r * s_inv % self.q
        r_ = pow(self.g, e1, self.p) * pow(self.y, e2, self.p) % self.p % self.q
        if r_ == r:
            return True
        else:
            return False


p = int(input("p: "))
q = int(input("q: "))
g = int(input("g: "))
y = int(input("y: "))
token = b'r7Au5njwTHEv01MxZ08TLxhuHtTn8rY1'

msg1 = bytes.fromhex('1111')
msg2 = bytes.fromhex('2222')

r1 = int(input("r1 of msg1 >> "))
s1 = int(input("sign of msg1 >> "))
r2 = int(input("r2 of msg2 >> "))
s2 = int(input("sign of msg2 >> "))

h1 = bytes_to_long(sha1(msg1).digest())
h2 = bytes_to_long(sha1(msg2).digest())

x = (s1 - s2) * inverse((h1 - h2), q) % q
k = inverse(x, q)

dsa = DSA(p, q, g, y, x, k)

print(dsa.sign(token))

print(hex(bytes_to_long(token)))
