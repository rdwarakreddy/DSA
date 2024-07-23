a = [7, 6, 4, 3, 1]
b = min(a)
c = a.index(b)
if len(a) == c + 1:
    print(0)
else:
    n = a[c + 1 :]
    ma = max(n)
    print(ma - b)

print(len(a))  # 6
