class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount = [-a for a in amount if a]
        heapq.heapify(amount)

        result = 0
        while amount:
            print(amount)
            a = heapq.heappop(amount)
            a += 1

            if amount:
                b = heapq.heappop(amount)
                b += 1
                if b:
                    heapq.heappush(amount, b)

            if a:
                heapq.heappush(amount, a)
            result += 1
        return result
