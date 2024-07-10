class Queue:
    def __init__(self):
        self.items = []

    # def __str__(self):
    #     values = []
    #     for i in self.items:
    #         values.append(str(i))
    #     return " ".join(values)

    def get_list(self):
        return self.items

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.items == []:
            return None
        else:
            return self.items.pop(0)

    def Peek(self):
        if self.items == []:
            return None
        else:
            return self.items[0]

    def delete(self):
        self.items = None


cq = Queue()
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
print(cq.get_list())
cq.dequeue()
print(cq.get_list())
print(cq.dequeue())
