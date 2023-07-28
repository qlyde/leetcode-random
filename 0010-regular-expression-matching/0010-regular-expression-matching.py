class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(si, pi):
            if si >= len(s) and pi >= len(p):
                return True
            if pi >= len(p):
                return False

            match = si < len(s) and (s[si] == p[pi] or p[pi] == ".")
            if pi + 1 < len(p) and p[pi + 1] == "*":
                return dfs(si, pi + 2) or (match and dfs(si + 1, pi))

            if match:
                return dfs(si + 1, pi + 1)
            return False
        return dfs(0, 0)
