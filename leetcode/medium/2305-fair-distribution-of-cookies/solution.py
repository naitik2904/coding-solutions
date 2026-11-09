# Complexity	Value
# Time:  O(kⁿ * k)
# Space: O(n + k)

class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        n = len(cookies)
        result = float('inf')
        children = [0] * k

        cookies.sort(reverse=True)

        def solve(idx: int):
            nonlocal result

            if(idx >= n):
                maxChild = max(children)
                result = min(result, maxChild)
                return
            
            cookie = cookies[idx]
            seen = set()

            for i in range(0, k):

                if children[i] in seen:
                    continue

                seen.add(children[i])

                children[i] += cookie

                solve(idx + 1)

                children[i] -= cookie
               

        solve(0)

        return result
        