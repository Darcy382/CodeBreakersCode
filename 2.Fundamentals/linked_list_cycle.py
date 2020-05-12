class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# First Attempt
def hasCycle(self, head: ListNode) -> bool:
    if head:
        slow = head.next
        if slow:
            fast = head.next.next
        else:
            return False
    else:
        return False

    while fast:
        if fast is slow:
            return True
        else:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return False