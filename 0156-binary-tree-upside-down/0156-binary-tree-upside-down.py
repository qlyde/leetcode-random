# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(node, parent, right):
            if not node:
                return parent
            res = recurse(node.left, node, node.right)
            node.right = parent
            node.left = right
            return res
        return recurse(root, None, None)
        
        