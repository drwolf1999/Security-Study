key1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
key2 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e ^ key1 # key2^key1 ^ key1 -> key2
key3 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 ^ key2 # key2^key3 ^ key2 -> key3

flag = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf ^ key1 ^ key2 ^ key3

s_flag = str(hex(flag))[2:]


print(bytes.fromhex(s_flag))