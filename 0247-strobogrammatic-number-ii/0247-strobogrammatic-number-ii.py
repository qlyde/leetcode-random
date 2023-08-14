class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
      m = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6"
      }

      result = []
      def backtrack(n, curr):
        if len(curr) > n:
          return
        if len(curr) == n and ((n == 1) or (n > 1 and curr[0] != "0")):
          result.append(curr)
          return

        for num in m:
          backtrack(n, num + curr + m[num])

      if n % 2 != 0:
        for num in m:
          if num == m[num]:
            backtrack(n, num)
      else:
        backtrack(n, "")
      
      return result
  