class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i, n):
            print(i, n)
            if i >= len(n):
                return 0
            return max(n[i] + dp(i + 2, n), dp(i + 1, n))
        return max(dp(0, tuple(nums[:-1]) if len(nums) > 1 else tuple(nums)), dp(1, tuple(nums)))

