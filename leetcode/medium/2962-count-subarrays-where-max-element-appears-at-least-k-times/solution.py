# TC: O(n)

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        maxNum = float(-inf)
        for num in nums:
            maxNum = max(maxNum, num)
        
        i = j = 0
        count = 0
        ans = 0

        while(j < n):

            curr = nums[j]
            if(curr == maxNum):
                count += 1
            
            while(count >= k):

                ans += (n - j)

                prev = nums[i]
                if(prev == maxNum):
                    count -= 1
                
                i += 1
            
            j += 1
        
        return ans
        