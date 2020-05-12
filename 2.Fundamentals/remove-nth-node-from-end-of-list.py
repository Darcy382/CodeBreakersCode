

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

