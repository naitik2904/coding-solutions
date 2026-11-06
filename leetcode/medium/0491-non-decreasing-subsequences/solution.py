# Time: O(n * 2^n) upper bound.
# Auxiliary space: O(n), excluding output.

class Solution:

    def solve(self, i: int, nums: list[int]):

        if(len(self.currList) > 1):
            self.resultList.append(self.currList.copy())
        
        Set = set()

        for j in range(i, self.n):

            if nums[j] in Set:
                continue
            
            if(len(self.currList) == 0 or self.currList[len(self.currList) - 1] <= nums[j]):

                Set.add(nums[j])
                self.currList.append(nums[j])

                self.solve(j + 1, nums)

                self.currList.pop()


    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        self.n = len(nums)
        self.currList = []
        self.resultList = []

        self.solve(0, nums)

        return self.resultList
        