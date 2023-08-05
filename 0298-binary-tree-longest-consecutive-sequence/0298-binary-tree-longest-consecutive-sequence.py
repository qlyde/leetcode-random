# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def dfs(node, prev=None, curr=0):
            nonlocal ret
            if not node:
                return
            if prev is not None and node.val != prev + 1:
                ret = max(ret, 1)
                dfs(node.left, node.val, 1)
                dfs(node.right, node.val, 1)
            else:
                ret = max(ret, curr + 1)
                dfs(node.left, node.val, curr + 1)
                dfs(node.right, node.val, curr + 1)
        dfs(root)
        return ret
