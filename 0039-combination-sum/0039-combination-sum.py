class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def backtrack(i, curr, currSum):
            if currSum == target:
                ret.append(list(curr))
                return
            if i >= len(candidates) or currSum > target:
                return
            backtrack(i, curr + [candidates[i]], currSum + candidates[i])
            backtrack(i + 1, curr, currSum)
        backtrack(0, [], 0)
        return ret
