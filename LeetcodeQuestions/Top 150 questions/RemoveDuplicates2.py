class Solution(object):
    def removeDuplicates(self, a):
        b = {}
        for i in a:
            if i not in b:
                b[i] = a.count(i)
        # print(b)  # {0: 2, 1: 4, 2: 1, 3: 2}
        for key, value in b.items():
            if value > 2:
                while a.count(key) > 2:
                    a.remove(key)
        return len(a)
