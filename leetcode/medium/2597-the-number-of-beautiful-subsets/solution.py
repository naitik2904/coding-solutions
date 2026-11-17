# Time Complexity: O(n * 2ⁿ)
# Space Complexity: O(n)

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        list = []

        def solve(idx: int):
            nonlocal result

            if(idx >= n):
                result += 1
                return
            
            # Skip
            solve(idx + 1)

            # Take
            isPresent = True

            for num in list:
                
                if((nums[idx] + k == num) or (nums[idx] - k == num)):
                    isPresent = False
                    break
            
            if(isPresent):

                list.append(nums[idx])

                solve(idx + 1)

                list.pop()

        solve(0)
        return result - 1   # Remove Empty Subset