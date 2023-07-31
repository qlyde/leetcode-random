class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ret = []
        def backtrack(i, curr, currSum):
            if currSum == target:
                ret.append(list(curr))
                return
            
            if i >= len(candidates) or currSum > target:
                return

            backtrack(i + 1, curr + [candidates[i]], currSum + candidates[i])

            i += 1
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1
            backtrack(i, curr, currSum)

        backtrack(0, [], 0)
        return ret

        