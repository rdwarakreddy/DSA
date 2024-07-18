class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
fanta = TreeNode("Fanta")
apple = TreeNode("Apple")
coke = TreeNode("Coke")
Pepsi = TreeNode("Pepsi")
newBT.leftChild = cold
newBT.rightChild = hot
cold.leftChild = fanta
cold.rightChild = apple
hot.leftChild = coke
hot.rightChild = Pepsi


def preOrder(RootNode):
    if not RootNode:
        return
    print(RootNode.data)
    preOrder(RootNode.leftChild)
    preOrder(RootNode.rightChild)


def InOrder(RootNode):
    if RootNode is None:
        return
    InOrder(RootNode.leftChild)
    print(RootNode.data)
    InOrder(RootNode.rightChild)


def postOrder(RootNode):
    if RootNode is None:
        return
    postOrder(RootNode.leftChild)
    postOrder(RootNode.rightChild)
    print(RootNode.data)
