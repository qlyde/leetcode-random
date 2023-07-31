# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q, d = deque(), 1
        q.append(root)

        while q:
            for _ in range(len(q)):
                n = q.popleft()
                if not n:
                    continue
                if not n.left and not n.right:
                    return d
                q.append(n.left)
                q.append(n.right)
            d += 1

        return -1
