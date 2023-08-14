# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def insert(head, node):
            dummy = ListNode(next=head)
            prev, curr = dummy, head
            while curr:
                if curr.val > node.val:
                    break
                prev = curr
                curr = curr.next
            prev.next, node.next = node, curr
            return dummy.next

        result = None
        curr = head
        while curr:
            tmp = curr.next
            result = insert(result, curr)
            curr = tmp
        return result
