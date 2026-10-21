class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        maxSum = float('-inf')
        sum = 0

        for i in range(0, n):

            sum += nums[i]
            maxSum = max(sum, maxSum)
            
            if(sum < 0):
                sum = 0

        return maxSum
        