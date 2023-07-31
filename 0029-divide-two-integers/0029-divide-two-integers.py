class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        HALF_MIN_INT = -1073741824

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        s = -1 if (divisor < 0) != (dividend < 0) else 1
        dividend = -abs(dividend)
        divisor = -abs(divisor)

        q = 0
        while divisor >= dividend:
            exp = -1
            val = divisor
            while val >= HALF_MIN_INT and val + val >= dividend:
                val += val
                exp += exp
            q += exp
            dividend -= val

        return abs(q) * s
