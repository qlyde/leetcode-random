class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diags = set()
        rdiags = set()

        def canPlace(row, col):
            if col in cols or row + col in diags or col - row in rdiags:
                return False
            return True

        def place(row, col):
            cols.add(col)
            diags.add(row + col)
            rdiags.add(col - row)

        def remove(row, col):
            cols.remove(col)
            diags.remove(row + col)
            rdiags.remove(col - row)

        ret = 0
        def backtrack(row):
            nonlocal ret
            for col in range(n):
                if canPlace(row, col):
                    if row == n - 1:
                        ret += 1
                    place(row, col)
                    backtrack(row + 1)
                    remove(row, col)

        backtrack(0)
        return ret

