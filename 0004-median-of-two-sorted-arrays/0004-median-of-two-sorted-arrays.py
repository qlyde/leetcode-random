class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1): return self.findMedianSortedArrays(nums2, nums1)

        l, r = 0, len(nums1)

        while l <= r:
            p1 = (l + r) // 2
            p2 = (len(nums1) + len(nums2) + 1) // 2 - p1

            l1 = nums1[p1 - 1] if p1 else float("-inf")
            l2 = nums2[p2 - 1] if p2 else float("-inf")
            r1 = nums1[p1] if p1 < len(nums1) else float("inf")
            r2 = nums2[p2] if p2 < len(nums2) else float("inf")

            if l1 <= r2 and l2 <= r1:
                if (len(nums1) + len(nums2)) & 1:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2)) / 2

            if l1 > r2:
                r = p1 - 1
            else:
                l = p1 + 1

        return -1