class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# First attempts
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = [Node("dummy") for _ in range(100)]

    def __str__(self):
        out = ""
        for i in range(len(self.array)):
            out += str(i) + "| "
            current = self.array[i].next
            while current:
                out += str(current.value) + " "
                current = current.next
            out += "\n"
        return out

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % 100
        current = self.array[index]
        while current.next:
            if current.value[0] == key:
                current.value[1] = value
                return
            current = current.next
        current.next = Node((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % 100
        current = self.array[index].next
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % 100
        current = self.array[index]
        prev = None
        while current.next:
            if current.value[0] == key:
                if prev:
                    prev.next = current.next
                else:
                    self.array[index] = current.next
                return
            prev = current
            current = current.next
h = MyHashMap()
h.put(1, 1)
print(h)
print(h.get(1))
