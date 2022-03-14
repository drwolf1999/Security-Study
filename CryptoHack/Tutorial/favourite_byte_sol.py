h = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

r = bytes.fromhex(h)

for b in range(256):
    res_bit = [e ^ b for e in r]
    res = "".join(chr(e) for e in res_bit)
    if 'crypto' in res:
        print(res)
        break