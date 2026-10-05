class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def sub(i: int) -> int:
            if i in cache:
                return cache[i]

            if i >= len(s):
                return 1

            is_valid_prefix = 1 <= int(s[i]) <= 9
            if not is_valid_prefix:
                return 0
            cache[i] = sub(i + 1)

            is_valid_group = (i + 1) < len(s) and (int(s[i]) == 1 or (int(s[i]) == 2 and 0 <= int(s[i + 1]) <= 6))
            if is_valid_group:
                cache[i] += sub(i + 2)
            
            return cache[i]
        
        return sub(0)