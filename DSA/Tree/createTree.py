class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children if children is not None else []

    def addChildren(self, treeNode):
        self.children.append(treeNode)

    def __str__(self, level=0):
        indent = " " * level * 2 + str(self.data) + "\n"
        for child in self.children:
            indent += child.__str__(level + 1)
        return indent


# Example usage
tree = TreeNode("Drinks")
cold = TreeNode("Cold")
hot = TreeNode("Hot")
tree.addChildren(cold)
tree.addChildren(hot)
fanta = TreeNode("Fanta")
apple = TreeNode("Apple")
cold.addChildren(fanta)
cold.addChildren(apple)
coke = TreeNode("Coke")
Pepsi = TreeNode("Pepsi")
hot.addChildren(coke)
hot.addChildren(Pepsi)

print(tree)
