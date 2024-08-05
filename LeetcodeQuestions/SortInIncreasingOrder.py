a = [1, 1, 2, 2, 3]
b = []
res = []
for i in a:
    c = a.count(i)
    b.append([i, c])
print(b)
d = dict(b)
for keys, values in d.items():
    print(keys, values)
