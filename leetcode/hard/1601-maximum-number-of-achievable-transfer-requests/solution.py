# TC: O(2^m * (m + n))
# SC: O(m + n)

class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        m = len(requests)
        result = float('-inf')

        resultant = [0] * n


        def solve(idx: int, count: int):
            nonlocal result

            if(idx >= m):
                allZero = True

                for r in resultant:
                    if(r != 0):
                        allZero = False
                
                if(allZero):
                    result = max(result, count)
                
                return
            

            src  = requests[idx][0]
            dest = requests[idx][1]

            resultant[src]  -= 1
            resultant[dest] += 1

            solve(idx + 1, count + 1)

            resultant[src]  += 1
            resultant[dest] -= 1

            solve(idx + 1, count)


        solve(0, 0)
        return result
        