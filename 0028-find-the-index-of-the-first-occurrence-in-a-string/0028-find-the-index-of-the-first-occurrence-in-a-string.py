class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP: O(n + m)
        m, n = len(needle), len(haystack)
        if n < m:
            return -1

        # pre-processing
        lps = [0] * m
        prev, i = 0, 1
        while i < m:
            if needle[i] == needle[prev]:
                prev += 1
                lps[i] = prev
                i += 1
            else:
                if prev == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prev = lps[prev - 1]

        # searching
        hp = np = 0
        while hp < n:
            if haystack[hp] == needle[np]:
                np += 1
                hp += 1
                if np == m:
                    return hp - m
            else:
                if np == 0:
                    hp += 1
                else:
                    np = lps[np - 1]

        return -1

