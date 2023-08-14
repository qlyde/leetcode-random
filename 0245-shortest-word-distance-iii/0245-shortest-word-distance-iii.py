class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
      result = float("inf")
      prev = -1
      for i, word in enumerate(wordsDict):
        if word == word1 or word == word2:
          if prev != -1:
            if word1 == word2 or wordsDict[i] != wordsDict[prev]:
              result = min(result, i - prev)
          prev = i

      return result
