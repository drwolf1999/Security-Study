s = 'label'

ns = ''

for e in s:
    ns += chr(ord(e) ^ 13)

print(ns)