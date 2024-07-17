a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b = []
for i in range(len(a)):
    b.append(a[i].count(1))
min = b.index(min(b))
print(min + 1)
