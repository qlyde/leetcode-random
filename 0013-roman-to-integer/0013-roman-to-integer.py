class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        ret = 0
        prev = float("-inf")
        for i in range(len(s) - 1, -1, -1):
            if m[s[i]] < prev:
                ret -= m[s[i]]
            else:
                ret += m[s[i]]
            prev = m[s[i]]
        return ret
