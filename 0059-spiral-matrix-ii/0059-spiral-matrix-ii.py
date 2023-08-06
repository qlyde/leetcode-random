class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #  1  2  3  4  5
        # 17 18 19 20  7
        # 16 25 26 21  8
        # 15 24 23 22  9
        # 14 13 12 11 10
        res = [[0] * n for _ in range(n)]
        curr = 1
        for layer in range((n + 1) // 2):
            # top
            for i in range(layer, n - layer):
                res[layer][i] = curr
                curr += 1

            # right
            for i in range(layer + 1, n - layer):
                res[i][n - layer - 1] = curr
                curr += 1

            # bottom
            for i in range(n - layer - 2, layer - 1, -1):
                res[n - layer - 1][i] = curr
                curr += 1

            # left
            for i in range(n - layer - 2, layer, -1):
                res[i][layer] = curr
                curr += 1

        return res
