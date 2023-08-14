class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localSum = globalSum = nums[0]
        for num in nums[1:]:
            localSum = max(num, localSum + num)
            globalSum = max(globalSum, localSum)
        return globalSum