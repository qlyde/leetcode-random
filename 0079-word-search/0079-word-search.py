class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(r, c, word):
            if not word:
                return True
            if r < 0 or r == len(board) or c < 0 or c == len(board[0]) or board[r][c] != word[0]:
                return False
            board[r][c] = "#"
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if backtrack(r + dr, c + dc, word[1:]):
                    return True
            board[r][c] = word[0]
            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and backtrack(r, c, word):
                    return True
        return False

