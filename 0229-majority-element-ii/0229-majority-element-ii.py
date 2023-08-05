class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ret = []
        n = len(nums) // 3
        for num, count in Counter(nums).items():
            if count > n:
                ret.append(num)
        return ret