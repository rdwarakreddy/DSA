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

    def appendAtFirst(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1

    def appendAtLocation(self, value, index):
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        new_node = Node(value)
        if index == 0:
            self.appendAtFirst(value)
        elif index == self.length:
            self.appendAtLast(value)
        else:
            temp_node = self.head
            for i in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1

    def Traversal(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                print(self.head.value)
                break

    def SearchwithValue(self, value):
        temp_node = self.head
        index = 0
        if self.length == 0:
            print("Value not found")
        while temp_node is not None:
            if temp_node.value == value:
                print(f"Value {value} found at index {index}")
            temp_node = temp_node.next
            index += 1
            if temp_node == self.head:
                break
        print(f"Value {value} not found")

    def SearchWithIndex(self, index):
        temp_node = self.head
        if index > self.length - 1 or index < 0:
            print("Index Out of range")
        else:
            for i in range(index):
                temp_node = temp_node.next
            print(temp_node.value)

    def UpdateValue(self, value, index):
        if index < 0 or index >= self.length:
            print("Index out of range")
        else:
            temp_node = self.head
            for i in range(index):
                temp_node = temp_node.next
            temp_node.value = value
            print(f"Value at index {index} updated to {value}")

    def PopFirst(self):
        if self.head is None:
            return "No elements in the List"
        temp_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp_node.next
            temp_node.next = None
            self.tail.next = self.head
        self.length -= 1
        return temp_node.value

    def PopAtEnd(self):
        if self.head is None:
            return "No elements in the List"
        popped_node = self.tail
        temp_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            while temp_node.next is not popped_node:
                temp_node = temp_node.next
            self.tail.next = None
            self.tail = temp_node
            self.tail.next = self.head
        self.length -= 1

    def RemoveAnyValue(self, index):
        temp_node = self.head
        if self.head is None:
            return "No elements in the List"
        if index < 0 or index >= self.length:
            return "Index is out of range"
        if index == 0:
            return self.PopFirst()
        for i in range(index - 1):
            temp_node = temp_node.next
        popped_node = temp_node.next
        if popped_node == self.tail:
            self.tail = temp_node
        temp_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node.value

    def deleteAllNodes(self):
        self.tail.next = None
        self.head = None
        self.tail = None


csLL = CSLinkedList()
csLL.appendAtLast(10)
csLL.appendAtLast(20)
csLL.appendAtLast(30)
csLL.appendAtLast(50)
print(csLL)
print(csLL.deleteAllNodes())
print(csLL)
