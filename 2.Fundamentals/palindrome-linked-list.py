

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# First attempt, O(N) time and space
def isPalindrome(self, head: ListNode) -> bool:
    current = head
    lst = []
    while current:
        lst.append(current.val)
        current = current.next

    for i in range(len(lst) // 2):
        if lst[i] != lst[-(i + 1)]:
            return False
    return True

# Second attempt and Third attempt, O(N) time, O(1) space
def isPalindrome2(self, head: ListNode) -> bool:
    # Get len of list
    cur = head
    length = 0
    while cur:
        length += 1
        cur = cur.next

    half_len = length // 2

    # reverse the first half
    prev = None
    cur = head
    for i in range(half_len):
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    # Compare the first and second half
    p1 = prev
    p2 = cur

    if length % 2 != 0:
        p2 = p2.next

    for i in range(half_len):
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next

    return True



