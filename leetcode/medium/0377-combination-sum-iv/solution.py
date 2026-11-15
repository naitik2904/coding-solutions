# TC: O(N * Target)
# SC: O(Target)

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        n = len(nums)
        dp = {}
        

        def solve(sum: int)-> int:

            if(sum == target):
                return 1
            
            if(sum > target):
                return 0
            
            if sum in dp:
                return dp[sum]

            count = 0
            for i in range(0, n):

                sum += nums[i]

                count += solve(sum)

                sum -= nums[i]
            
            dp[sum] = count
            return count

        return solve(0)        