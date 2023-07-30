# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        l = r = dummy
        for _ in range(n + 1):
            r = r.next # n <= sz

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next
        return dummy.next
