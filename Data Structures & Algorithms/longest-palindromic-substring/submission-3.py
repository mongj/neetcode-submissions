class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        # best[start][end] is the longest palindrome inside s[start:end + 1]
        best: list[list[tuple[int, int]]] = [[(0, 0) for _ in range(n)] for _ in range(n)]

        for length in range(1, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                if length == 1 or (length == 2 and s[start] == s[end]):
                    best[start][end] = (start, end)
                    continue

                # case 1: s[start:end] is a palindrome
                if (
                    length >= 3
                    and s[start] == s[end]
                    and best[start + 1][end - 1] == (start + 1, end - 1)
                ):
                    best[start][end] = (start, end)
                    continue

                # case 2: check substrings
                ls, le = best[start][end - 1]
                rs, re = best[start + 1][end]
                if (le - ls) > (re - rs):
                    best[start][end] = (ls, le)
                else:
                    best[start][end] = (rs, re)

        s_start, s_end = best[0][n - 1]
        return s[s_start:s_end + 1]