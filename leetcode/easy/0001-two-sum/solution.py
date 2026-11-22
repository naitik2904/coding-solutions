# TC: O(n)
# SC: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        map = {}
        ans = []

        for i in range(0, n):

            first = nums[i]
            second = target - first

            if(second in map):
                ans.append(i)
                ans.append(map[second])

                return ans
            
            map[first] = i
        
        return ans
        