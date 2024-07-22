a = [2, 3, 4]
b = []
res = 1
for i in a:
    res *= i
    b.append(res / i)
print(b)
