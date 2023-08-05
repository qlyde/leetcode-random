class Solution:
    def jump(self, nums: List[int]) -> int:
        ret = 0
        end = far = 0
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if i == end:
                ret += 1
                end = far
        return ret

# 2,3,1,1,4
# i = 0:   far = 2, end = 2, ret = 1
# i = 1:   far = 4, end = 2, ret = 1
# i = 2:   far = 4, end = 4, ret = 2
# i = 3:   far = 4, end = 4, ret = 2