class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        ret = 0
        heapify(sticks)
        while len(sticks) > 1:
            a, b = heappop(sticks), heappop(sticks)
            ret += a + b
            heappush(sticks, a + b)
        return ret
