class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if nums == [0] * len(nums):
            return "0"
        def cmp(a, b):
            return -1 if a + b < b + a else (1 if a + b > b + a else 0)
        return "".join(sorted([str(num) for num in nums], key=cmp_to_key(cmp), reverse=True))
