class Solution(object):
    def isValid(self, a):
        b = list(a)
        c = {"(": ")", "[": "]", "{": "}"}

        stack = []

        for i in b:
            if i in c.keys():
                stack.append(i)
            elif i in c.values():
                if stack and c[stack[-1]] == i:
                    stack.pop()
                else:
                    print(False)
                    break
        else:
            if not stack:
                return True
            else:
                return False
