class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        idx = 0

        for i in range(0, n):

            if(nums[i] % 2 == 0):
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1

        return nums