class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# First attempt O(N) time and space
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        new_nodes = {}
        og_ids = {}

        i = 0
        cur = head
        while cur:
            new_nodes[i] = Node(cur.val)
            og_ids[id(cur)] = i
            cur = cur.next
            i += 1

        i = 0
        cur = head
        while cur:
            # Set the next pointer
            if cur.next:
                new_nodes[i].next = new_nodes[i + 1]

            # Find rand index
            if cur.random is not None:
                rand_idx = og_ids[id(cur.random)]
                new_nodes[i].random = new_nodes[rand_idx]

            cur = cur.next
            i += 1

        return new_nodes[0]

def copyRandomList(head):
    if head is None:
        return None
    # First pass to set values and record the id -> node index
    nodes = {}
    id_indicies = {}
    cur = head
    i = 0
    while cur:
        nodes[i] = Node(cur.val)
        id_indicies[id(cur)] = i
        cur = cur.next
        i += 1

    # second pass to set the next and the random pointer
    cur = head
    i = 0
    while cur.next:
        nodes[i] = nodes[i + 1]
        if cur.random:
            random_index = id_indicies[id(cur.random)]
            nodes[i] = random_index
        cur = cur.next
        i += 1
    if cur.random:
        random_index = id_indicies[id(cur.random)]
        nodes[i] = random_index

    return nodes[0]