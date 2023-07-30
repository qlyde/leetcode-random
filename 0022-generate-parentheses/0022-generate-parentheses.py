class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # open: open < n
        # close: close < open
        ret = []
        def backtrack(n, o=0, c=0, curr=""):
            if n == o == c:
                ret.append(curr)
                return
            if o < n:
                backtrack(n, o + 1, c, curr + "(")
            if c < o:
                backtrack(n, o, c + 1, curr + ")")

        backtrack(n)
        return ret
