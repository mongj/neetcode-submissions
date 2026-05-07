class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.isPalindrome(s, True)
    
    def isPalindrome(self, s: str, canDelete: bool) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif canDelete:
                return self.isPalindrome(s[l+1:r+1], False) or self.isPalindrome(s[l:r], False)
            else:
                return False
        return True