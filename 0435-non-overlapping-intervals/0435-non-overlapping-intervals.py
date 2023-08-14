class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
      intervals.sort() # [[1,2], [1,3], [2,3], [3,4]]
      result = 0
      prev = intervals[0]
      for i in range(1, len(intervals)):
        curr = intervals[i]
        if curr[0] < prev[1]: # overlap
          # if overlap, keep interval with lesser end
          if curr[1] < prev[1]:
            prev = curr
          result += 1
        else:
          prev = curr
      return result
