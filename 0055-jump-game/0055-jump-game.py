class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp[i] = dp[i+1] || ... || dp[i+nums[i]]
        dp = [False] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                dp[i] = True
                continue
            reachable = False
            for j in range(1, nums[i] + 1):
                if i + j < len(nums) and dp[i + j]:
                    reachable = True
                    break
            dp[i] = reachable
        return dp[0]
