#!/usr/bin/python3
from Crypto.Util.number import getPrime
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import hashlib
import random

class Person(object):
    def __init__(self, p):
        self.p = p
        self.g = 2
        self.x = random.randint(2, self.p - 1)
    
    def calc_key(self):
        self.k = pow(self.g, self.x, self.p)
        return self.k

    def set_shared_key(self, k):
        self.sk = pow(k, self.x, self.p)
        aes_key = hashlib.md5(str(self.sk).encode()).digest()
        self.cipher = AES.new(aes_key, AES.MODE_ECB)

    def encrypt(self, pt):
        return self.cipher.encrypt(pad(pt, 16)).hex()

    def decrypt(self, ct):
        return unpad(self.cipher.decrypt(bytes.fromhex(ct)), 16)




# p = 0x8da6039b34d43889b9132b3ff3a7468cdff6b09fcd78075346c55fe5738f005f068ed298cf7adad2b79deb8a5a4feca2d84a10f19a1cebd539b734a993b93c6a4163e54695e6ec4ea036aeafa6b34ebf89d1a5626d68a4c7be1de75c5a8a309572bc8511e0fe4c0e1818a3bc506f71a495212d05d5605b90493d941c2d6bf533
p = int(input("prime >> "), 16)
wa = Person(p)
wb = Person(p)
a = int(input("alice key >> "), 16)
print('attacker to Bob', wb.calc_key())
# b = 0x6832928fd0431587d0bd88c1b9cb3863ec478cb500c3f14c5a92984196839d72dad2da7ac4aa8a9c33f485a77fd864b8b24865cfe0ab9cda58e9006d44a9ee3a82013b13e662c64c1ae42bc19e4923f221a6b89fbc27064b756626d0895ea08ea5499856410d6a485b2a0c6fa4c21de1fe25c5cd64f2519707c95f32d0be797a
wa.set_shared_key(a)

# a = 0x1940fafc14118f3caa46af7bfac8a8e6cfac4b4f02aa7bbfc8589a25888996bb16329979d4865d3de2b28ea2a45da5ecacba62200f35213333eecd40a59d695e816e62a3f21e6d08d29420ea55b0fd267bd375c0bc818af7cbbd567c44f02f00aac93d9effed8281d404cf4ff2e2757573fb5662ed08fefed9f9e1d21282343
b = int(input("bob key >> "), 16)
print('atacker to Alice', wa.calc_key())
wb.set_shared_key(b)

ac = input("alice cipher >> ")
bc = input("bob cipher >> ")


print(wa.decrypt(ac))
print(wb.decrypt(bc))