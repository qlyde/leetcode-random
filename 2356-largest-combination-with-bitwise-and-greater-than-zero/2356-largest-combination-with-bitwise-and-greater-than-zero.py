class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # generate 24 sums, 1 for each bit positions, then count number of candidates with this bit set
        return max(sum(n & (1 << i) > 0 for n in candidates) for i in range(0, 24))
        