# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ret = []
        reverse = False
        q = deque([root])
        while q:
            level, l = [0] * len(q), len(q)
            for i in range(l):
                n = q.popleft()
                if reverse:
                    level[l - i - 1] = n.val
                else:
                    level[i] = n.val

                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            ret.append(level)
            reverse = not reverse
        return ret
