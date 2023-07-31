# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def heightBalanced(root):
            if not root: return True, 0
            lb, ld = heightBalanced(root.left)
            rb, rd = heightBalanced(root.right)
            return abs(ld - rd) <= 1 and lb and rb, 1 + max(ld, rd)

        return heightBalanced(root)[0]
        