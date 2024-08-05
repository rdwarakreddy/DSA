class Solution(object):
    def sortPeople(self, a, b):
        c = []
        b_copy = b[:]
        for i in range(len(b_copy)):
            d = max(b_copy)
            ind = b_copy.index(d)
            c.append(a[ind])
            b_copy[ind] = -1  # Use -1 to avoid confusion with 0 height

        return c


names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
sol = Solution()
print(sol.sortPeople(names, heights))
