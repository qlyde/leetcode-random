class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        res = curr = -1
        for i in range(1, len(nums)):
            if curr > 0 and nums[i] == nums[i - 2]:
                curr += 1
            else:
                curr = 2 if nums[i] == nums[i - 1] + 1 else -1
            res = max(res, curr)
        return res