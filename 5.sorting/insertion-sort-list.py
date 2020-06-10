# def insertionSortList(self, head: ListNode) -> ListNode:
#     if head is None:
#         return None
#
#     insert_node = head.next
#     sorted_end = head
#     while insert_node:
#         cur = head
#         prev = None
#         while cur is not insert_node:
#             if insert_node.val > cur.val:
#                 prev = cur
#                 cur = cur.next
#             else:  # insert_node.val <= cur.val
#                 if prev:
#                     prev.next = insert_node
#                 else:
#                     head = insert_node
#                 sorted_end.next = insert_node.next
#                 insert_node.next = cur
#                 break
#         if cur is insert_node:
#             sorted_end = insert_node
#
#         insert_node = sorted_end.next
#
#     return head
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insertionSortList2(head):
    '''
         p    c
    1 -> 2 -> 3 -> 4
                  ls
                     i

    '''
    if head is None:
        return None

    last_sorted = head
    insert_node = head.next
    while insert_node:
        prev = None
        cur = head
        print("last_sorted", last_sorted.val)
        while cur is not insert_node:
            print("current ", cur.val)
            print("insert_node", insert_node.val)
            if insert_node.val <= cur.val:
                last_sorted.next = last_sorted.next.next
                if prev:
                    prev.next = insert_node
                    insert_node.next = cur
                else:
                    insert_node.next = head
                    head = insert_node

                break
            else:
                prev = cur
                cur = cur.next
        if cur is insert_node:
            last_sorted = last_sorted.next

        insert_node = last_sorted.next
    return head

head = Node(4)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)

insertionSortList2(head)