class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
      @cache
      def dp(currSum):
        if currSum == target:
          return 1
        if currSum > target:
          return 0
        return sum(dp(currSum + num) for num in nums)
      return dp(0)
