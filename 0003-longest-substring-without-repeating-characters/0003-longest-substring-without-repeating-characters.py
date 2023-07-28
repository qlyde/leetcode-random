class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        st = set()
        ret = 0
        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[l])
                l += 1
            st.add(s[r])
            ret = max(r - l + 1, ret)
        return ret
