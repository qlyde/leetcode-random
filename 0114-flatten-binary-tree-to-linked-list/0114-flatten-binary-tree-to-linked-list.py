# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        def preorder(root):
            if not root:
                return
            stack.append(root)
            preorder(root.left)
            preorder(root.right)

        preorder(root)

        prev = None
        while stack:
            n = stack[-1]
            stack.pop()

            n.left = None
            n.right = prev
            prev = n
