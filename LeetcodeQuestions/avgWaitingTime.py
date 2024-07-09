A = [[1, 2], [2, 5], [4, 3]]
finishingTime = 0
WaitingTime = 0
wt = []
for i in range(len(A)):
    if i == 0:
        b = sum((A[int(i)]))
        finishingTime = b
        WaitingTime = finishingTime - (A[int(i)][0])
        wt.append(WaitingTime)
    else:
        b = finishingTime + A[i][1]
        finishingTime = b
        WaitingTime = finishingTime - A[i][0]
        wt.append(WaitingTime)
res = sum((wt)) / len(A)
print(f"{res:.5f}")
