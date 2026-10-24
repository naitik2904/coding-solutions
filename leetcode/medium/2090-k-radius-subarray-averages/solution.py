# TC: O(n)

class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        if k == 0:
            return nums

        n = len(nums)
        ans = [-1] * n

        windowSize = 2 * k + 1

        if windowSize > n:
            return ans
        
        start = k
        sum = 0

        for i in range(0, windowSize):
            sum += nums[i]
        
        ans[start] = sum // windowSize
        start += 1

        for i in range(windowSize, n):

            sum += nums[i] - nums[i - windowSize]
            ans[start] = sum // windowSize

            start += 1
        
        return ans