# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, target):
            if not root.left and not root.right: # leaf
                return target - root.val == 0
            if not root.left:
                return dfs(root.right, target - root.val)
            if not root.right:
                return dfs(root.left, target - root.val)
            return dfs(root.left, target - root.val) or dfs(root.right, target - root.val)
        return root and dfs(root, targetSum)
