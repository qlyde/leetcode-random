class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        multi = 5
        while n >= multi:
            res += n // multi
            multi *= 5
        return res