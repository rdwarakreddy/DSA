class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        results = ""
        while temp_node is not None:
            results += str(temp_node.value)
            if temp_node.next is not None:
                results += "<->"
            temp_node = temp_node.next
        return results

    def appendAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def appendAtBegining(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def Travsersal(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next

    def ReverseTraversal(self):
        temp_node = self.tail
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.prev


DLL = DoubleLinkedList()
DLL.appendAtBegining(0)
DLL.appendAtBegining(1)
DLL.appendAtBegining(2)
DLL.appendAtBegining(3)
print(DLL)
DLL.ReverseTraversal()
