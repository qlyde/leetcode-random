class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ret, closest = 0, float("inf")
        nums.sort()

        # -4, -1, 1, 2
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < closest:
                    closest = abs(s - target)
                    ret = s

                if s == target:
                    return s
                elif s < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return ret

