class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)

        currList = []
        resultList = []

        candidates.sort()
        
        def solve(idx: int, sum: int):
            nonlocal currList
            nonlocal resultList

            if sum == target:
                resultList.append(currList.copy())
                return
            
            if sum > target:
                return
            
            for i in range(idx, n):

                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                currList.append(candidates[i])

                solve(i + 1, sum + candidates[i])

                currList.pop()

        solve(0, 0)
        return resultList
        