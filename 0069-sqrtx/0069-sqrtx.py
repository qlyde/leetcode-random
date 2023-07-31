class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x // 2 + 1
        while l <= r:
            m = l + (r - l) // 2
            sq = m * m
            if sq == x:
                return m
            elif sq < x:
                l = m + 1
            else:
                r = m - 1
        return r

