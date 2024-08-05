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
            if a[i] != "null":
                self.Nodes[i] = TreeNode(int(a[i]))  # Ensure value is an integer
            else:
                self.Nodes[i] = None

        for i in range(len(a)):
            if self.Nodes[i] is not None:
                left = 2 * i + 1
                right = 2 * i + 2
                if left < len(self.Nodes) and self.Nodes[left] is not None:
                    self.Nodes[i].left = self.Nodes[left]
                if right < len(self.Nodes) and self.Nodes[right] is not None:
                    self.Nodes[i].right = self.Nodes[right]

    def get_list(self):
        res = []
        for i in self.Nodes:
            if i is not None:
                res.append(i.val)
            else:
                res.append(None)
        return res

    def validateBST(self, root):
        if root is None:
            return True
        if root.left is not None and root.left.val >= root.val:
            return False
        if root.right is not None and root.right.val <= root.val:
            return False
        if (
            root.left is not None
            and root.right is not None
            and root.left.val == root.val
            and root.right.val == root.val
        ):
            return False
        return self.validateBST(root.left) and self.validateBST(root.right)


a = [5, 4, 6, "null", "null", 3, 7]
low = 7
high = 15
L = List()
L.ArraytoTree(a)
print(L.get_list())  # Print node values including None
root = L.Nodes[0]
print(L.validateBST(root))
