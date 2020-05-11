class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, listNode):
        #head references first node in chain of nodes
        self.head = listNode

    def __repr__(self):
        current = self.head
        output = ""
        while current:
            output += str(current.value)
            output += "|"
            current = current.next
        return output

    __str__ = __repr__

    def insertBeginning(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def insertEnd(self, newNode):
        if self.head is None:
          self.head = new_node
          return
        cur = self.head
        while(cur.next):
          cur = cur.next
        cur.next = newNode

    def deleteFront(self):
        if self.head:
          self.head = self.head.next


ll = LinkedList(Node(1))
ll.insertBeginning(Node(2))
ll.insertEnd(Node(3))
ll.deleteFront()
print(ll)
