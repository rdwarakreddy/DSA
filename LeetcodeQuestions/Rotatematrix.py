a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose_a = list(zip(*a))
new = []
for i in transpose_a:
    b = list(i[::-1])
    new.append(b)
print(new)
