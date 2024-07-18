a = [1, 2, 3, 4, 5, 6, 7]
k = 3
b = a[-k:]
a[-k:] = []
print(a + b)
print(type(a))
