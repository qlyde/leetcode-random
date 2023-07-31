class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                if nums[l] > nums[r] and nums[m] > nums[r] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[l] > nums[r] and nums[m] < nums[l] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

# 3,1    1