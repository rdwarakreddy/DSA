a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
b = set()
i = 0
while i < len(a):
    if a[i] in b:
        del a[i]
    else:
        b.add(a[i])
        i += 1
print(len(a))
