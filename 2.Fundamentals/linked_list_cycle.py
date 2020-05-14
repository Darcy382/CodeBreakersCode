class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# First Attempt  O(n) time and  O(1) space
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

# Second attempt: time = O(N) space = O(1)
def hasCycle(self, head: ListNode) -> bool:
    try:
        slow = head.next
        fast = head.next.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False
