#!/usr/bin/python3
from random import randrange
from Crypto.Util.number import getStrongPrime, bytes_to_long, inverse, long_to_bytes


class RSA(object):
    def __init__(self):
        self.p = getStrongPrime(512)
        self.q = getStrongPrime(512)
        self.N = self.p * self.q
        self.e = 0x10001
        self.d = inverse(self.e, self.N - self.p - self.q + 1)

    def encrypt(self, pt):
        return pow(pt, self.e, self.N)

    def decrypt(self, ct):
        return pow(ct, self.d, self.N)


n = 137498999070682421294314472636259414163535599895670250430630479629203814182510339307302008649084799006444312529699626628313268236632503249929424631175031809261827762757123717679359434991562894632385220281480852854436604110548272172310574817351222113909071082551751440863553807019918667687309166436003036374001
e = 65537
c = 131211073589829859230267370104666484475995279739043505508076749277277126507106203422661473132565620598750415086293158032559809794126551242423796121035499126881199049871408322910983020025382479256162364879665282926314864389827407215771385174439728614407011483556914803598528749745074332651714510988231516368089

r = 2
y = (pow(r, e, n) * c) % n
print(y)


d = 265303025271760754782762668660255715813910508769429152493707039977108929146371416679674
p = (inverse(r, n) * d) % n
print(p)
print(long_to_bytes(p))

# 132651512635880377391381334330127857906955254384714576246853519988554464573185708339837
# 2F5A160879949D4CCD2D4FA188B8258F478C663834E8A8CC5048A98986CD2FBB93A93FA9BA4E7F4B7EA19E40323093E4FE8C73CF40131811611A27E79BC1C85BAD5C329D93EF04A176D9E98EC6DB62DD1A061103F4A99D2DA3062C733D415B9B49DD87225A407EF3AD5914260EA54DD4D5AE96BF2D799B6B1C5240F9C1670E40
# 89195473397297113500413983960164707399018601151547137359126306695262654379506985426733856891188416739990938313801366424678859817884937064492562621125823392039647111285566595919059672862448718985300434494161971523120192288182215437587238945089030870694339092097680070847662581937329216029977226218321089461080

# rsa = RSA()
# FLAG = bytes_to_long(open("flag", "rb").read())
# FLAG_enc = rsa.encrypt(FLAG)

# print("Welcome to dream's RSA server")

# while True:
#     print("[1] Encrypt")
#     print("[2] Decrypt")
#     print("[3] Get info")

#     choice = input()

#     if choice == "1":
#         print("Input plaintext (hex): ", end="")
#         pt = bytes_to_long(bytes.fromhex(input()))
#         print(rsa.encrypt(pt))

#     elif choice == "2":
#         print("Input ciphertext (hex): ", end="")
#         ct = bytes_to_long(bytes.fromhex(input()))
#         if ct == FLAG_enc or ct > rsa.N:
#             print("Do not cheat !")
#         else:
#             print(rsa.decrypt(ct))

#     elif choice == "3":
#         # print(f"N: {rsa.N}")
#         # print(f"e: {rsa.e}")
#         # print(f"FLAG: {FLAG_enc}")
#         print("N: %d" % rsa.N)
#         print("e: %d" % rsa.e)
#         print("FLAG: %d" % FLAG_enc)

#     else:
#         print("Nope")
