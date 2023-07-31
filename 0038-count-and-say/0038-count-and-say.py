class Solution:
    def countAndSay(self, n: int) -> str:
        def say(n):
            r = ""
            count, curr = 0, ""
            for c in n:
                if curr != c:
                    if count: r += str(count) + curr
                    count, curr = 1, c
                else:
                    count += 1
            return r + str(count) + curr

        r = "1"
        for _ in range(n - 1):
            r = say(r)
        return r
