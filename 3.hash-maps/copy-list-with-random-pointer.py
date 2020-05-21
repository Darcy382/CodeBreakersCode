
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