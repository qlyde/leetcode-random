class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        #    1,   2,   4,   6   k = 2
        # -1,3  0,4  2,6  4,8
        ret = l = 0
        for r in range(len(nums)):
            # if min(r) > max(l), invalid => move len
            # nums[r] - k > nums[l] + k
            # nums[r] - nums[l] > 2k
            while nums[r] - nums[l] > 2 * k:
                l += 1
            ret = max(ret, r - l + 1)
        return ret
