# Word Search

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an `m x n` grid of characters `board` and a string `word`, return `true`  *if*  `word`  *exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

 **Example 1:** 

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

```

 **Example 2:** 

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

```

 **Example 3:** 

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

```

 

 **Constraints:** 

- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.

 

 **Follow up:**  Could you use search pruning to make your solution faster with a larger `board`?

## Solution

**Language:** Python  
**Runtime:** 3338 ms (beats 81.73%)  
**Memory:** 19.3 MB (beats 76.04%)  
**Submitted:** 2026-10-29T14:22:52.459Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/word-search/)