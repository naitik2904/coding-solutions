# TC: O(n)

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        last_zero_idx = -1
        ans = float('-inf')
        i = j = 0

        while(j < n):

            if(nums[j] == 0):
                i = last_zero_idx + 1
                last_zero_idx = j
            

            ans = max(ans, j - i)
            j += 1
        
        return ans

        