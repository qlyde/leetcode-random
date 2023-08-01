class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        substrLen = wordLen * len(words)
        if substrLen > len(s):
            return []

        targetWordCounts = collections.defaultdict(int)
        for word in words:
            targetWordCounts[word] += 1

        ret = []
        def slidingWindow(s, i):
            windowWordCounts = collections.defaultdict(int)
            l = 0
            for r in range(len(s)):
                if (r - l + 1) % wordLen == 0:
                    word = s[r - wordLen + 1:r + 1]
                    if word not in targetWordCounts:
                        l = r + 1
                        windowWordCounts = collections.defaultdict(int)
                    else:
                        windowWordCounts[word] += 1
                        if r - l + 1 == substrLen:
                            if targetWordCounts == windowWordCounts:
                                ret.append(l + i)
                            windowWordCounts[s[l:l + wordLen]] -= 1
                            l += wordLen
                
        for i in range(wordLen):
            slidingWindow(s[i:], i)

        return ret

