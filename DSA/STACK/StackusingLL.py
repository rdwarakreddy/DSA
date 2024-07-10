class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_nodes(self):
        nodes = []
        curNode = self.head
        while curNode:
            nodes.append(curNode)
            curNode = curNode.next
        return nodes


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = []
        for node in self.LinkedList.get_nodes():
            values.append(str(node.value))
        return "\n".join(values)

    def isEmpty(self):
        return self.LinkedList.head is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.LinkedList.head
        self.LinkedList.head = new_node

    def Pop(self):
        if self.isEmpty():
            return None
        else:
            popped_node = self.LinkedList.head
            self.LinkedList.head = self.LinkedList.head.next
            popped_node.next = None

    def Peek(self):
        if self.isEmpty():
            return None
        else:
            return self.LinkedList.head.value

    def delete(self):
        self.LinkedList.head = None


cs = Stack()
print(cs.isEmpty())  # Output: True
cs.push(10)
cs.push(20)
cs.push(30)
print(cs)  # Output: 30\n20\n10
cs.Pop()
print(cs)
print(cs.Peek())
