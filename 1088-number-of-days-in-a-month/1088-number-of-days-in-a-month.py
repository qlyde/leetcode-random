class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
      thirtyOne = set([1, 3, 5, 7, 8, 10, 12])
      thirty = set([4, 6, 9, 11])
      if month in thirtyOne:
        return 31
      if month in thirty:
        return 30
      if year % 4 != 0:
        return 28
      if year % 100 != 0:
        return 29
      if year % 400 == 0:
        return 29
      return 28