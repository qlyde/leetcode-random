class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def canAdd(d, r, c):
            return d not in rows[r] and d not in cols[c] and d not in sqs[(r // 3, c // 3)]

        def addDigit(d, r, c):
            rows[r].add(d)
            cols[c].add(d)
            sqs[(r // 3, c // 3)].add(d)
            board[r][c] = str(d)

        def removeDigit(d, r, c):
            rows[r].discard(d)
            cols[c].discard(d)
            sqs[(r // 3, c // 3)].discard(d)
            board[r][c] = "."

        def next(r, c):
            if c == 8 and r == 8:
                nonlocal solved
                solved = True
            else:
                if c == 8:
                    backtrack(r + 1, 0)
                else:
                    backtrack(r, c + 1)

        def backtrack(r, c):
            if board[r][c] == ".":
                for d in range(1, 10):
                    if canAdd(d, r, c):
                        addDigit(d, r, c)
                        next(r, c)
                        if not solved:
                            removeDigit(d, r, c)
            else:
                next(r, c)

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqs = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    addDigit(int(board[r][c]), r, c)

        solved = False
        backtrack(0, 0)
