class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if j > 0 and nums[j] == nums[j - 1]:
                continue
            nums[i] = nums[j]
            i += 1
        return i