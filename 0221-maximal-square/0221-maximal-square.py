class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ret = 0
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 2)]
        for r in range(1, len(matrix) + 1):
            for c in range(1, len(matrix[0]) + 1):
                if matrix[r - 1][c - 1] == "1":
                    dp[r][c] = min(dp[r - 1][c], min(dp[r - 1][c - 1], dp[r][c - 1])) + 1
                ret = max(ret, dp[r][c] ** 2)
        return ret
