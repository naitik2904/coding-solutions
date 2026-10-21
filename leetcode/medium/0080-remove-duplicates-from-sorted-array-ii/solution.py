class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        start = 2

        for i in range(2, n):
            if(nums[start - 2] != nums[i]):
                nums[start] = nums[i]
                start += 1
        
        return start
        