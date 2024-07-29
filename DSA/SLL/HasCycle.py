class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result

    def appendLast(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def ReverseLL(self):
        prev = None
        current = self.head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def HasCycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next  # Move slow pointer by 1 step
            fast = fast.next.next  # Move fast pointer by 2 steps

            if slow == fast:
                return True  # Cycle detected

        return False  # No cycle detected


# Initialize the linked list and test
new_linkedList = LinkedList()
new_linkedList.appendLast(10)
new_linkedList.appendLast(20)
new_linkedList.appendLast(30)

print(new_linkedList)  # Output: 10->20->30

# Test for cycle
print("Cycle exists:" if new_linkedList.HasCycle() else "No cycle")

# To create a cycle, you could manually link the last node to a previous node
new_linkedList.tail.next = new_linkedList.head.next  # Create a cycle

print("Cycle exists:" if new_linkedList.HasCycle() else "No cycle")
