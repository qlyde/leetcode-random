# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head
        
        l, curr = 1, head
        while curr.next:
            l += 1
            curr = curr.next
        curr.next = head
        k = l - (k % l)

        curr = head
        for _ in range(k - 1):
            curr = curr.next
        curr.next, newRoot = None, curr.next

        return newRoot
        