# Time Complexity: O(k * C(n, k))

# Space Complexity:
# - Auxiliary Space: O(k)
# - Output Space: O(k * C(n, k))
# - Total Space: O(k * C(n, k))


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        currList = []
        resultList = []


        def solve(idx: int):
            nonlocal currList
            nonlocal resultList

            if(len(currList) == k):
                resultList.append(currList.copy())
            
            for i in range(idx, n + 1):

                currList.append(i)

                solve(i + 1)

                currList.pop()

        
        solve(1)
        return resultList
        