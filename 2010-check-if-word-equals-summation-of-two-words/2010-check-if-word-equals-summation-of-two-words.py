class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def toInt(word):
            ret = 0
            for ch in word:
                ret = ret * 10 + ord(ch) - ord("a")
            return ret

        return toInt(firstWord) + toInt(secondWord) == toInt(targetWord)
