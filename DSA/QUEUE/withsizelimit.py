class Queue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.items = []
        self.start = 0
        self.top = 0

    def get_list(self):
        return self.items

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.items) == self.maxSize:
            return True
        else:
            False

    def enqueue(self, value):
        if self.isFull():
            print("Queue is full")
        else:
            self.items.append(value)
            if len(self.items) == 1:
                self.start = 0
                self.top = 0
            else:
                self.top += 1
        if self.top == self.maxSize:
            print("Queue is Full")

    def dequeue(self):
        self.start += 1
        self.top -=1
        return self.items.pop(0)

    def Peek(self):
        return self.items[0]


cq = Queue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.enqueue(6)
print(cq.get_list())
print(cq.dequeue())
print(cq.get_list())
print(cq.Peek())
cq.enqueue(6)
print(cq.dequeue())
print(cq.dequeue())
cq.enqueue(10)
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
cq.enqueue(10)
