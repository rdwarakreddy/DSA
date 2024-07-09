class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        results = ""
        while temp_node is not None:
            results += str(temp_node.value)
            results += "<->"
            temp_node = temp_node.next
            if temp_node == self.head:
                results += str(temp_node.value)
                break
            # else:
            #     results += "<->"
        return results

    def appendAtLast(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length += 1

    def appendAtBegining(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length += 1

    def Traversal(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                print(temp_node.value)
                break

    def ReversalTraversal(self):
        temp_node = self.tail
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.prev
            if temp_node == self.tail:
                print(temp_node.value)
                break

    def SearchWithValue(self, value):
        if self.length == 0:
            return None
        temp_node = self.head
        index = 0
        while temp_node is not None:
            if temp_node.value == value:
                return index
            else:
                temp_node = temp_node.next
                if temp_node == self.head:
                    break
                index += 1

    def SearchWithIndex(self, index):
        temp_node = self.head
        for i in range(index):
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return temp_node.value


CDLL = CircularDoubleLinkedList()
CDLL.appendAtBegining(10)
CDLL.appendAtLast(1)
CDLL.appendAtLast(2)
CDLL.appendAtLast(300)
CDLL.appendAtLast(4)
CDLL.appendAtLast(5)
print(CDLL)
print(CDLL.SearchWithIndex(3))
