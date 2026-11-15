class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)

        currList = []
        resultList = []

        def solve(idx: int, sum: int):
            nonlocal currList
            nonlocal resultList

            if(sum == target):
                resultList.append(currList.copy())
                return
            
            if(sum > target):
                return
            
            for i in range(idx, n):

                currList.append(candidates[i])

                solve(i, sum + candidates[i])

                currList.pop()

        solve(0, 0)
        return resultList
        