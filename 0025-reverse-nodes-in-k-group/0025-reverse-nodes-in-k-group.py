# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def linkedListLength(self, head):
        n, curr = 0, head
        while curr:
            n += 1
            curr = curr.next
        return n

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if self.linkedListLength(head) < k:
            return head

        prev, curr = head, head.next
        for _ in range(k - 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        head.next = self.reverseKGroup(curr, k)
        return prev
