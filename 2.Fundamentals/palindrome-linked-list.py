

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# First attempt O(N) time and space
class Solution:
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