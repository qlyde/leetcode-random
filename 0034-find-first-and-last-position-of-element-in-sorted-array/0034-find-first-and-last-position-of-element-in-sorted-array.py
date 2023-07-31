class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, second = -1, -1

        # first occurrence
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                if m == 0 or nums[m] != nums[m - 1]:
                    first = m
                    break
                else:
                    r = m - 1

        # second occurrence
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                if m == len(nums) - 1 or nums[m] != nums[m + 1]:
                    second = m
                    break
                else:
                    l = m + 1

        return [first, second]
