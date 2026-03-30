class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        groups = [0] * k

        def backtrack(i):
            nonlocal ans
            if i == len(cookies):
                ans = min(ans, max(groups))
                return

            for j in range(k):
                groups[j] += cookies[i]

                if groups[j] < ans:
                    backtrack(i + 1)

                groups[j] -= cookies[i]
        backtrack(0)
        return ans