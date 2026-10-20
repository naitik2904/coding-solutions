# TC: O(n)

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []
        ans.append(nums[0])

        for i in range (1, n):
            num = nums[i] + ans[i - 1]
            ans.append(num)
        
        return ans
        