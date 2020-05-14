

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# First Attempt
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None

        queue = []
        max_size = n + 1
        current = head

        while current:
            if len(queue) == max_size:
                queue.pop(0)
            queue.append(current)
            current = current.next

        try:
            prev = queue[-max_size]
            prev.next = prev.next.next
        except:
            head = head.next

        return head

# Second attempt, Two pass solution time O(N), space O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Two pass solution
        # Find length of list
        if head is None:
            return None
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        # Find the removal index
        rem_inx = length - n

        # edge case for removing head
        if rem_inx == 0:
            return head.next

        # iterate to the node prior to the removal node
        current = head
        for i in range(rem_inx - 1):
            current = current.next

        # Remove the nth node
        current.next = current.next.next

        return head