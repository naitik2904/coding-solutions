# Time Complexity: O(m * n * 4^L)
# Auxiliary Space Complexity: O(L) ; L = length of word.

class Solution:
    def solve(self, i: int, j: int, idx: int,  board: list[list[str]], word: str):
        if(idx == len(word)):
            return True

        if(i < 0 or i >= self.m or j < 0 or j >= self.n):
            return False
        
        if(board[i][j] != word[idx]):
            return False

        temp = board[i][j]
        board[i][j] = '$'

        found = (
                    self.solve(i + 1, j, idx + 1, board, word) or
                    self.solve(i - 1, j, idx + 1, board, word) or
                    self.solve(i, j + 1, idx + 1, board, word) or
                    self.solve(i, j - 1, idx + 1, board, word)
                )
        
        board[i][j] = temp

        return found

    def exist(self, board: list[list[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])

        for i in range(0, self.m):
            for j in range(0, self.n):

                if(board[i][j] == word[0]):
                    if(self.solve(i, j, 0, board, word)):
                        return True
                    
        return False