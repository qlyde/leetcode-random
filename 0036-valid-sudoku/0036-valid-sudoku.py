class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqs = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue

                if (
                    cell in rows[r] or
                    cell in cols[c] or
                    cell in sqs[r // 3][c // 3]
                ):
                    return False

                rows[r].add(cell)
                cols[c].add(cell)
                sqs[r // 3][c // 3].add(cell)
        return True
        
        