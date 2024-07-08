# Check if a Circular Linked List is Sorted
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

    def checkIfSorted(self):
        temp_node = self.head
        next_node = self.head.next
        while temp_node is not self.tail:
            if temp_node.value > next_node.value:
                return "The LinkedList is not sorted"
            elif (
                temp_node.value < next_node.value or temp_node.value == next_node.value
            ):
                temp_node = temp_node.next
                next_node = next_node.next
        return "Linked List is Sorted"


csLL = CSLinkedList()
csLL.appendAtLast(3)
csLL.appendAtLast(1)
csLL.appendAtLast(4)
csLL.appendAtLast(2)
csLL.appendAtLast(3)
print(csLL)
print(csLL.checkIfSorted())
