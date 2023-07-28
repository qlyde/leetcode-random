class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n: return True

        i = 0
        while i < len(flowerbed):
            if flowerbed[i]:
                i += 2
                continue
        
            l = i - 1 < 0 or not flowerbed[i - 1]
            r = i + 1 >= len(flowerbed) or not flowerbed[i + 1]
            if l and r:
                i += 2
                n -= 1
                if not n:
                    return True
            else:
                i += 1
        return False
