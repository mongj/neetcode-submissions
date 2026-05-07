class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l: int, r: int, canDelete: bool) -> bool:
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                elif canDelete:
                    return isPalindrome(l + 1, r, False) or isPalindrome(l, r - 1, False)
                else:
                    return False
            return True
        
        l = 0
        r = len(s) - 1
        return isPalindrome(l, r, True)