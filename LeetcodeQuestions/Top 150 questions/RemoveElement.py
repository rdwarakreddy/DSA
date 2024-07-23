nums = [3, 2, 2, 3]
val = 3
i = 0
for x in nums:
    if x != val:
        nums[i] = x
        i += 1
print((i))
