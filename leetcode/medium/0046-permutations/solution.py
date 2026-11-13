# TC: O(N * N!)
# Auxiliary SC: O(N)
# Total SC including output: O(N * N!).

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)

        seen = set()
        currList = []
        resultList = []

        def solve():
            nonlocal currList
            nonlocal resultList

            if(len(currList) == n):
                resultList.append(currList.copy())
            
            for i in range(0, n):

                if nums[i] in seen:
                    continue
                
                seen.add(nums[i])
                currList.append(nums[i])

                solve()

                seen.remove(nums[i])
                currList.pop()

        solve()
        return resultList
        