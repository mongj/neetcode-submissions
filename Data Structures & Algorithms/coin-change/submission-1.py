class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_sentinel = amount + 1
        coins.sort()
        cache = {}

        def change(remaining: int) -> int:
            if remaining in cache:
                return cache[remaining]

            if remaining == 0:
                return 0
            if remaining < coins[0]:
                return max_sentinel
            
            cache[remaining] = 1 + min([change(remaining - val) for val in coins])
            return cache[remaining]

        ans = change(amount)
        return ans if ans < max_sentinel else -1