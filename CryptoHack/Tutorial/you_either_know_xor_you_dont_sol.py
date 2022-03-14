encrypt_msg = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

encrypt_msg = bytes.fromhex(encrypt_msg)

# flag 형태
flag = b'crypto{'

# flag 와 encrypt_msg를 xor해서 key를 구함
key = [e1 ^ e2 for (e1, e2) in zip(encrypt_msg, flag)] + [ord('y')]

key_l = len(key)
flag = ''
# key를 통해 flag구하기
for i in range(len(encrypt_msg)):
    flag += chr(encrypt_msg[i] ^ key[i % key_l])
print(flag)