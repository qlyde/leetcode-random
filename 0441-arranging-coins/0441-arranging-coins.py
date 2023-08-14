class Solution:
    def arrangeCoins(self, n: int) -> int:
      # 1 + 2 + ... + k = k(k+1)/2
      # max k such that k(k+1)/2 <= N
      #
      # k(k+1) <= 2N
      # k^2 + k <= 2N
      # (k + 1/2)^2 - 1/4 <= 2N
      # (k + 1/2)^2 <= 2N + 1/4
      # k = floor(sqrt(2N + 1/4) - 1/2)
      return (int)((2 * n + 0.25) ** 0.5 - 0.5)
