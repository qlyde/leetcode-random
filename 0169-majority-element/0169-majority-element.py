class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer-moore voting algo: O(n) time, O(1) space
        count, candidate = 0, 0
        for n in nums:
            if count == 0: candidate = n
            count += 1 if candidate == n else -1
        return candidate
