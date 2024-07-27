class Solution(object):
    def findRestaurant(self, a, b):
        c = {}
        res = []
        for i in a:
            if i in b:
                d = (a.index(i)) + (b.index(i))
                c[i] = d
        min_val = min(c.values())
        for keys, val in c.items():
            if val == min_val:
                res.append(keys)
        return res
