class Solution(object):
    def numTeams(self, a):
        count = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                for k in range(j + 1, len(a)):
                    if a[i] > a[j] > a[k] or a[i] < a[j] < a[k]:
                        count += 1
        return count
