class Solution:
    def myAtoi(self, s: str) -> int:
        n, i, sign = 0, 0, 1

        while (i < len(s) and s[i].isspace()):
            i += 1

        if (i < len(s) and (s[i] == "-" or s[i] == "+")):
            sign = 1 if s[i] == "+" else -1
            i += 1

        while (i < len(s) and s[i].isnumeric()):
            n = n * 10 + int(s[i])
            i += 1
        
        n *= sign
        if n < 0: return max(-(2 ** 31), n)
        return min(2 ** 31 - 1, n)
