# Split a Circular Linked List into Two Equal Halves
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        if self.head is None:
            return "List is empty"
        while True:
            result += str(temp_node.value)
            temp_node = temp_node.next
            result += "->"
            if temp_node == self.head:
                result += str(temp_node.value)
                break
            # else:
            #     result += "->"
        return result

    def appendAtLast(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def SearchWithIndex(self, index):
        temp_node = self.head
        if index > self.length - 1 or index < 0:
            print("Index Out of range")
        else:
            for i in range(index):
                temp_node = temp_node.next
            print(temp_node.value)

    def GetLength(self):
        return self.length // 2

    def TwoHalves(self):
        l = self.length // 2
        firstHalf = CSLinkedList()
        secondhalf = CSLinkedList()
        temp_node = self.head
        for i in range(l):
            firstHalf.appendAtLast(temp_node.value)
            temp_node = temp_node.next
        for i in range(l):
            secondhalf.appendAtLast(temp_node.value)
            temp_node = temp_node.next
        return firstHalf, secondhalf


csLL = CSLinkedList()
csLL.appendAtLast(10)
csLL.appendAtLast(20)
csLL.appendAtLast(30)
csLL.appendAtLast(40)
print(csLL)
csLL.SearchWithIndex(4)
print(csLL.GetLength())
a, b = csLL.TwoHalves()
print(a)
print(b)
