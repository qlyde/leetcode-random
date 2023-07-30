class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        s, pre = strs[0], ""

        for i in range(len(s)):
            for word in strs[1:]:
                if i >= len(word) or word[i] != s[i]:
                    return pre
            pre += s[i]

        return pre

