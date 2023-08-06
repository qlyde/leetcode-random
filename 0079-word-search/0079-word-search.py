class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(r, c, i):
            if i == len(word):
                return True
            if r not in range(len(board)) or c not in range(len(board[0])) or board[r][c] != word[i]:
                return False
            board[r][c] = "#"
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if backtrack(r + dr, c + dc, i + 1):
                    return True
            board[r][c] = word[i]
            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True
        return False
                