class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# First Attempt
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    currentA = headA
    currentB = headB
    id_set = set()

    while currentA or currentB:
        if currentA:
            old_length = len(id_set)
            id_set.add(id(currentA))
            if len(id_set) == old_length:
                return currentA
            currentA = currentA.next
        if currentB:
            old_length = len(id_set)
            id_set.add(id(currentB))
            if len(id_set) == old_length:
                return currentB
            currentB = currentB.next
    return None



