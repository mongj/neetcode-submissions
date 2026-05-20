class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        for char_s in s:
            # increment p until t[p] matches char
            # if we run out chars in t and s hasn't finished
            # then s is not a subsequence
            while p < len(t) and t[p] != char_s:
                p += 1
            if p == len(t):
                return False
            p += 1
        return True