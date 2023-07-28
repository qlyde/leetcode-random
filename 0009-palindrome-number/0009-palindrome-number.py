class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        c, r = x, 0
        while x:
            r = r * 10 + x % 10
            x //= 10
        return c == r
