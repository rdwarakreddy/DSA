a = [7, 6, 4, 3, 1]
b = min(a)
c = a.index(b)
if len(a) == c + 1:
    a.remove(b)
else:
    n = a[c + 1 :]
    ma = max(n)
    print(ma - b)
