# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stackL1 = []
        stackL2 = []
        while l1:
            stackL1.append(l1.val)
            l1 = l1.next
        while l2:
            stackL2.append(l2.val)
            l2 = l2.next

        curr = prev = None
        c = 0
        while stackL1 or stackL2 or c:
            a = stackL1[-1] if stackL1 else 0
            b = stackL2[-1] if stackL2 else 0

            s = a + b + c
            c = s // 10

            curr = ListNode(s % 10)
            curr.next = prev
            prev = curr

            if stackL1: stackL1.pop()
            if stackL2: stackL2.pop()

        return curr
