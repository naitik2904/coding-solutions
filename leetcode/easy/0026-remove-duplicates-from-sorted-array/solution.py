# TC: O(n)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        start = 0

        for i in range(1, n):
            if(nums[i - 1] != nums[i]):
                start += 1
                nums[start] = nums[i]

        return start + 1
        