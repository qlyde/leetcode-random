# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def sortedArrayToBST(nums):
            if not nums: return None
            m = len(nums) // 2
            return TreeNode(nums[m], sortedArrayToBST(nums[:m]), sortedArrayToBST(nums[m + 1:]))

        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return sortedArrayToBST(arr)
