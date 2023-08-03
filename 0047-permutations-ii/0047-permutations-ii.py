class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrack(perm, counter):
            if len(perm) == len(nums):
                ret.append(list(perm))
                return
            
            for num in counter:
                if counter[num]:
                    perm.append(num)
                    counter[num] -= 1
                    backtrack(perm, counter)
                    perm.pop()
                    counter[num] += 1

        backtrack([], collections.Counter(nums))
        return ret
