class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        # odd length palindromes
        for i in range(n):
            # take i as the center, then try to expand outwards
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        # even length
        for i in range(r-1):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count