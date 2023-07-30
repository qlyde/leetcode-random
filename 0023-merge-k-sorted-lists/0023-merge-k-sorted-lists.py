# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        pq = []

        for l in lists:
            while l:
                heapq.heappush(pq, l.val)
                l = l.next

        while pq:
            curr.next = ListNode(heapq.heappop(pq))
            curr = curr.next

        return dummy.next
