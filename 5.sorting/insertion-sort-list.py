def insertionSortList(self, head: ListNode) -> ListNode:
    if head is None:
        return None

    insert_node = head.next
    sorted_end = head
    while insert_node:
        cur = head
        prev = None
        while cur is not insert_node:
            if insert_node.val > cur.val:
                prev = cur
                cur = cur.next
            else:  # insert_node.val <= cur.val
                if prev:
                    prev.next = insert_node
                else:
                    head = insert_node
                sorted_end.next = insert_node.next
                insert_node.next = cur
                break
        if cur is insert_node:
            sorted_end = insert_node

        insert_node = sorted_end.next

    return head