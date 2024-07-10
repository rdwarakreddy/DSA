class Stack:
    def __init__(self):
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

    def push(self, value):
        self.list.append(value)
        return "The element is inserted"

    def Pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list.pop()

    def Peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list[-1]

    def delete(self):
        self.list = None


cs = Stack()
print(cs.isEmpty())
cs.push(1)
cs.push(2)
cs.push(3)
print(cs)
print(cs.Peek())
