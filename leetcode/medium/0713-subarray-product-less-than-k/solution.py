# TC: O(n)

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if(k <= 1):
            return 0
        
        n = len(nums)

        product = 1
        i = j = 0
        ans = 0

        while(j < n):

            product *= nums[j]

            while(product >= k):

                product /= nums[i]
                i += 1

            ans += (j - i + 1)
            j += 1
        
        return ans
        