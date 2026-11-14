# Time Complexity: O(n * 4ⁿ)
# Space Complexity: O(n * 4ⁿ) - including output
# Auxiliary Space: O(n)

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        n = len(digits)

        str = ""
        result = []

        map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        if n == 0:
            return result
        
        def solve(idx: int):
            nonlocal str
            nonlocal result

            if idx >= n:
                result.append(str)
                return
            
            digit = digits[idx]
            temp  = map.get(digit)

            for i in range(0, len(temp)):

                str += temp[i]

                solve(idx + 1)

                str = str[: -1]

        solve(0)
        return result
        