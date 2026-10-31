# TC: O(n)
# SC: O(K)

class Solution:
    def solve(self, nums: list[int], k: int) -> int:
        n = len(nums)

        i = j = 0
        count = 0
        map = {}

        while(j < n):

            curr = nums[j]
            map[curr] = map.get(curr, 0) + 1

            while(len(map) > k):

                prev = nums[i]
                map[prev] = map.get(prev) - 1

                if(map.get(prev) == 0):
                    map.pop(prev)
                
                i += 1
            
            count += (j - i + 1)
            j += 1
        
        return count

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        # Exactly K distinct → AtMost(K) - AtMost(K-1)

        atMost_K = self.solve(nums, k)
        atMost_k_minus_one = self.solve(nums, k - 1)

        exactlyK = atMost_K - atMost_k_minus_one

        return exactlyK
        