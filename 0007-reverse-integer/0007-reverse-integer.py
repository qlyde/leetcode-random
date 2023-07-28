class Solution:
    def reverse(self, x: int) -> int:
        imax, imin = 2 ** 31 - 1, -(2 ** 31)

        s = -1 if x < 0 else 1
        x *= s

        r = 0
        while x:
            r = r * 10 + x % 10
            x //= 10

            if r * s < imin or r * s > imax:
                return 0

        return r * s
