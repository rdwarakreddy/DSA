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


DLL = DoubleLinkedList()
DLL.appendAtEnd(1)
DLL.appendAtEnd(2)
DLL.appendAtEnd(3)

print(DLL)
