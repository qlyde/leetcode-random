# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []
        def dfs(n, s, curr):
            if not n.left and not n.right: # leaf
                if s + n.val == targetSum:
                    ret.append(curr + [n.val])
                return
            if n.right:
                dfs(n.right, s + n.val, curr + [n.val])
            if n.left:
                dfs(n.left, s + n.val, curr + [n.val])
        
        if not root:
            return []
        dfs(root, 0, [])
        return ret
