class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if nums == [0] * len(nums):
            return "0"

        def cmp(a, b):
            ai = bi = 0
            while ai < len(a) and bi < len(b):
                if int(a[ai]) > int(b[bi]):
                    return -1
                elif int(a[ai]) < int(b[bi]):
                    return 1
                else:
                    ai += 1
                    bi += 1
            if ai < len(a):
                return cmp(a[ai:], b)
            if bi < len(b):
                return cmp(a, b[bi:])
            return 0
        return "".join(sorted([str(num) for num in nums], key=cmp_to_key(cmp)))
