class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class List:
    def __init__(self):
        self.Nodes = []

    def ArraytoTree(self, a):
        if not a:
            return None
        self.Nodes = [None] * len(a)
        for i in range(len(a)):
            self.Nodes[i] = TreeNode(a[i])

        for i in range(len(a)):
            if self.Nodes[i] is not None:
                left = 2 * i + 1
                right = 2 * i + 2
                if left < len(self.Nodes) and self.Nodes[left] is not None:
                    self.Nodes[i].left = self.Nodes[left]
                elif right < len(self.Nodes) and self.Nodes[right] is not None:
                    self.Nodes[i].right = self.Nodes[right]
            # return self.Nodes

    def get_list(self):
        res = []
        for i in self.Nodes:
            if i is not None:
                res.append(i.val)
            else:
                res.append(None)
        return res

    def RangeSum(self, a, low, high):
        b = []
        for i in self.Nodes:
            if i is not None:
                if low < i < high:
                    b.append(i)
        return sum(b)


a = [10, 5, 15, 3, 7, "null", 18]
low = 7
high = 15
L = List()
(L.ArraytoTree(a))
print(L.get_list())
print(L.RangeSum(a, low, high))
