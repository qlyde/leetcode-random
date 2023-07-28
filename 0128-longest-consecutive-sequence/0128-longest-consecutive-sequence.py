class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ret, st = 0, set(nums)
        for n in nums:
            if n - 1 not in st:
                l = 0
                while n + l in st:
                    l += 1
                ret = max(ret, l)
        return ret