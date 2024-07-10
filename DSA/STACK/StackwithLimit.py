class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = []
        for i in reversed(self.list):
            values.append(str(i))
            # values.append((i))
        return "\n".join(values)
        # return values

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully added"

    def Pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list.pop()

    def Peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[-1]

    def delete(self):
        self.list = None


cs = Stack(5)
print(cs.isEmpty())
print(cs.isFull())
cs.push(1)
cs.push(2)
cs.push(3)
cs.push(4)
cs.push(5)
print(cs)
print(cs.isEmpty())
print(cs.isFull())
(cs.Pop())
print(cs)
