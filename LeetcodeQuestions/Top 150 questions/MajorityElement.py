a = [2, 2, 1, 1, 1, 2, 2]
b = int(len(a) / 2)
c = {}
for i in a:
    if i not in c:
        c[i] = a.count(i)
for key, value in c.items():
    if value > b:
        print(key)
