class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        def binarySearch(spell):
            l, r = 0, len(potions) - 1
            while l <= r:
                m = (l + r) // 2
                if potions[m] * spell >= success:
                    r = m - 1
                else:
                    l = m + 1
            return l

        result = []
        for spell in spells:
            result.append(len(potions) - binarySearch(spell))
        return result