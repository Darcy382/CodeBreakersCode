class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# First attempt
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


# Second Attempt
class MyHashMap2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 100
        self.hashTable = [[] for _ in range(self.capacity)]

    def __str__(self):
        out = ""
        for bucket in self.hashTable:
            out += str(bucket) + "\n"
        return out

    def hashFunction(self, key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # Get the bucket
        bucket = self.hashTable[self.hashFunction(key)]
        # Check if key is alreadly in map
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                # Update key's value if it is
                bucket[i] = (key, value)
                break

        # Otherwise add the key, value pair to the bucket
        bucket.append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        # Get the bucket
        bucket = self.hashTable[self.hashFunction(key)]
        # Check if key is in bucket
        for item in bucket:
            if item[0] == key:
                # Return it's value if it is
                return item[1]

        # Otherwise, return -1
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # Get the bucket
        bucket = self.hashTable[self.hashFunction(key)]
        # Find the key index in bucket
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return


h = MyHashMap2()
h.put(1, 1)
h.put(2, 2)
print(h.get(1))
print(h.get(3))
h.put(2, 1)
print(h.get(2))
# h.remove(2)
# h.remove(2)
print(h)
print(h.get(2))
