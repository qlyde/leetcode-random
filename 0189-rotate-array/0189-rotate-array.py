class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c, l = list(nums), len(nums)
        for i in range(len(nums)):
            nums[i] = c[(i - k) % l]
