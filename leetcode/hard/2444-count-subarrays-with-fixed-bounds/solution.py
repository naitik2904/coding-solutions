# TC: O(n)

class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        n = len(nums)

        minKPosition = -1
        maxKPosition = -1
        culpritPosition = -1
        ans = 0

        for i in range(0, n):

            if(nums[i] > maxK or nums[i] < minK):
                culpritPosition = i
            
            if(nums[i] == minK):
                minKPosition = i
            
            if(nums[i] == maxK):
                maxKPosition = i

            smaller = min(maxKPosition, minKPosition)

            temp = smaller - culpritPosition

            ans += 0 if temp < 0 else temp
        
        return ans
        