class Solution:
    def longestValidParentheses(self, s: str) -> int:
        opened = closed = 0
        ret = l = 0
        for r in range(len(s)):
            if s[r] == "(":
                opened += 1
            elif s[r] == ")":
                closed += 1
                if opened == closed:
                    ret = max(ret, r - l + 1)
                elif opened < closed:
                    l = r + 1
                    opened = closed = 0

        opened = closed = 0
        r = len(s) - 1
        for l in range(len(s) - 1, -1, -1):
            if s[l] == "(":
                opened += 1
                if opened == closed:
                    ret = max(ret, r - l + 1)
                elif opened > closed:
                    r = l - 1
                    opened = closed = 0
            elif s[l] == ")":
                closed += 1

        return ret
