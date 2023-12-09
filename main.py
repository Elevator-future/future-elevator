

n = int(input("Input numbers amount >>>"))
s, m = [], []
for _ in range(n):
    s.append(input())
for i in range(len(s)-1):
    a = int(s[i]) + int(s[i + 1])
    m.append(a)
print(m)








