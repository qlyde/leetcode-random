class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Rabin-Karp
        # AAAAACCCCC --> 0000011111
        # hash: 0*4^9 + 0*4^8 + ... + 1*4^1 + 1*4^0
        #
        #      *4 -> 0*4^10 + 0*4^9 + ... + 1*4^2 + 1*4^1
        # -0*4^10 ->          0*4^9 + ... + 1*4^2 + 1*4^1
        # +0*4^0  ->          0*4^9 + ... + 1*4^2 + 1*4^1 + 0*4^0 (AAAACCCCCA)
        m = {"A": 0, "C": 1, "G": 2, "T": 3}
        nums = [m[ch] for ch in s]

        ret = []
        h = 0
        seen = collections.defaultdict(int)
        for start in range(len(nums) - 10 + 1):
            if start == 0:
                for i in range(10):
                    h = h * 4 + nums[i]
            else:
                h = h * 4 - nums[start - 1] * pow(4, 10) + nums[start + 9]

            if h in seen and seen[h] == 1:
                ret.append(s[start:start + 10])
            seen[h] += 1
        return ret


