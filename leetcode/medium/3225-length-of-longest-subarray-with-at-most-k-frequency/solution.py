# Time: O(n) — each pointer moves forward at most n times.
# Space: O(n) — the HashMap can store up to n distinct elements.

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        map = {}
        i = j = 0
        subArray = 0
        maxSubArray = float('-inf')

        while(j < n):

            curr = nums[j]
            map[curr] = map.get(curr, 0) + 1

            while(map[curr] > k):

                prev = nums[i]
                map[prev] = map.get(prev) - 1

                i += 1
            
            subArray = j - i + 1
            maxSubArray = max(subArray, maxSubArray)

            j += 1
        
        return maxSubArray

        