class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        ret = []

        def getPerm(comb, counter):
            if len(comb) == len(s):
                ret.append(comb)
                return
            
            for letter in counter:
                if counter[letter]:
                    newCounter = counter.copy()
                    newCounter[letter] -= 2
                    getPerm(letter + comb + letter, newCounter)

        counter = Counter(s)
        odds = []
        for ch in counter:
            if counter[ch] % 2 != 0:
                odds.append(ch)
                counter[ch] -= 1

        if len(odds) > 1:
            return []

        getPerm(odds[0] if len(odds) else "", counter)
        return ret
    