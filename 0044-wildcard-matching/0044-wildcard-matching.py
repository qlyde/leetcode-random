class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ps = list(p)
        k = 0
        for i in range(len(p)):
            if i and p[i] == p[i - 1] == "*":
                continue
            ps[k] = p[i]
            k += 1
        p = "".join(ps[:k])

        @cache
        def backtrack(si, pi):
            if si >= len(s) and pi >= len(p):
                return True
            if pi >= len(p):
                return False
            if si >= len(s):
                return True if p[pi] == "*" and pi == len(p) - 1 else False
            if p[pi] == "?" or p[pi] == s[si]:
                return backtrack(si + 1, pi + 1)
            if p[pi] == "*":
                return backtrack(si + 1, pi) or backtrack(si, pi + 1)
            return False
        return backtrack(0, 0)
