class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ret = float("inf")
        l = windowSum = 0
        for r in range(len(nums)):
            windowSum += nums[r]
            while windowSum >= target:
                ret = min(ret, r - l + 1)
                windowSum -= nums[l]
                l += 1
        return ret if ret != float("inf") else 0
