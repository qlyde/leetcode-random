# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        l = r = dummy
        for _ in range(left - 1):
            l = l.next
        for _ in range(right + 1):
            r = r.next

        curr, prev = l.next, r
        while curr != r:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        l.next = prev
        return dummy.next