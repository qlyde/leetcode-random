class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s

        rows = [[] for _ in range(numRows)]
        row, d = -1, 1
        for ch in s:
            row += d
            rows[row] += ch
            if row == numRows - 1:
                d = -1
            elif row == 0:
                d = 1
        print(rows)
        return "".join(["".join(row) for row in rows])
