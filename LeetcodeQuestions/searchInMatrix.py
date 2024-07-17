a = [[1], [3]]
b = 3
c = 0
for i in range(len(a)):
    if b in a[i]:
        c += 1
if c == 1:
    print(True)
else:
    print(False)
