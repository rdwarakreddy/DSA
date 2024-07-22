class BinaryTree:
    def __init__(self, size):
        self.customsize = size * [None]
        self.lastusedindex = 0
        self.maxsize = size
        self.preo = []

    def insert(self, value):
        if self.lastusedindex + 1 == self.maxsize:
            return "The Tree is full"
        self.lastusedindex += 1
        self.customsize[self.lastusedindex] = value
        return f"{value} is inserted at {self.lastusedindex}"

    def get_list(self):
        return self.customsize

    def Search(self, value):
        index = 0
        for i in self.customsize:
            if i == value:
                return f"{value} found in {index}"
            else:
                index += 1
        return f"{value} not found"

    def PreOrder(self, index):
        if index > self.lastusedindex or self.customsize[index] is None:
            return
        self.preo.append(self.customsize[index])
        (self.PreOrder(index * 2))
        (self.PreOrder(index * 2 + 1))
        return self.preo

    def Inorder(self, index):
        if index > self.lastusedindex or self.customsize[index] is None:
            return
        (self.Inorder(index * 2))
        self.preo.append(self.customsize[index])
        (self.Inorder(index * 2 + 1))
        return self.preo

    def postOrder(self, index):
        if index > self.lastusedindex or self.customsize[index] is None:
            return
        (self.postOrder(index * 2))
        (self.postOrder(index * 2 + 1))
        self.preo.append(self.customsize[index])
        return self.preo

    def LevelOrder(self, index):
        Lo = []
        for i in range(index, self.lastusedindex):
            Lo.append(self.customsize[i])
        return Lo

    def delete(self, value):
        if self.lastusedindex == 0:
            return "The tree is empty"
        for i in range(1, self.lastusedindex + 1):
            if self.customsize[i] == value:
                self.customsize[i] = self.customsize[self.lastusedindex]
                self.customsize[self.lastusedindex] = None
                self.lastusedindex -= 1
                break


newBt = BinaryTree(8)
newBt.insert("Drinks")
newBt.insert("Cold")
newBt.insert("Hot")
newBt.insert("Fanta")
newBt.insert("Apple")
newBt.insert("Coke")
newBt.insert("Pepsi")
# print(newBt.get_list())
# print(newBt.Search("Cold"))
# print(newBt.LevelOrder(1))
# print(newBt.delete("Pepsi"))
print(newBt.LevelOrder(1))
