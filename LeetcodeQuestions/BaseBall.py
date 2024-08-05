a = ["5", "2", "C", "D", "+"]
b = []
for i in a:
    if i == "C":
        b.pop()
    elif i == "D":
        c = (b[-1]) * 2
        b.append(c)
    elif i == "+":
        c = (b[-1]) + (b[-2])
        b.append(c)
    elif i != "C" and "D" and "+":
        b.append(int(i))
print(sum(b))
