# First attempt and second attempt, O(1) time and space
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev = None
        self.next = None
        return self

    # Make a set method for value

class doublyList:
    def __init__(self):
        self.front = Node("front", "front")
        self.back = Node("back", "back")
        self.front.next = self.back
        self.back.prev = self.front

    def insertFront(self, new_node):
        old_first = self.front.next
        self.front.next = new_node
        new_node.prev = self.front
        new_node.next = old_first
        old_first.prev = new_node

    def removeLast(self):
        return self.back.prev.remove()


class LRUCache:

    def __init__(self, capacity: int):
        self.deque = doublyList()
        self.hash_table = {}
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.hash_table:
            node = self.hash_table[key]
            node.remove()
            self.deque.insertFront(node)
            return node.val # Use a getter method
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_table:
            node = self.hash_table[key]
            node.val = value # Use a set method 
            node.remove()
            self.deque.insertFront(node)
        else:
            if self.size == self.capacity:
                old_node = self.deque.removeLast()
                del self.hash_table[old_node.key]
            else:
                self.size += 1

            new_node = Node(key, value)
            self.hash_table[key] = new_node
            self.deque.insertFront(new_node)


