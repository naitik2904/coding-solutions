# Sliding Window
# TC: O(n)
# SC: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)

        s = set()
        i = j = 0

        while(j < n):

            if(abs(i - j) > k) :

                prevNum = nums[i]
                s.remove(prevNum)
                i += 1
            
            currNum = nums[j]

            if(currNum in s):
                return True
            
            s.add(currNum)
            j += 1
        
        return False

