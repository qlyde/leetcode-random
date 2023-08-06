class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maximumProduct = minimumProduct = nums[0]
        res = maximumProduct

        for num in nums[1:]:
            maximumProduct, minimumProduct = (
                max(num, minimumProduct * num, maximumProduct * num),
                min(num, minimumProduct * num, maximumProduct * num)
            )

            res = max(maximumProduct, res)

        return res
        