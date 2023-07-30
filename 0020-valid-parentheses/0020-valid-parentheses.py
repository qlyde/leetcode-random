class Solution:
    def isValid(self, s: str) -> bool:
        m = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for p in s:
            if p in m:
                stack.append(m[p])
            else:
                if not stack or stack[-1] != p:
                    return False
                stack.pop()
        return not stack
            