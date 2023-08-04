class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ret = 0
        def backtrack(i, currXor):
            nonlocal ret
            if i >= len(nums):
                ret += currXor
                return
            backtrack(i + 1, currXor ^ nums[i])
            backtrack(i + 1, currXor)
        backtrack(0, 0)
        return ret
