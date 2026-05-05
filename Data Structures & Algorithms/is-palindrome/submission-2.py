class Solution:
    def isPalindrome(self, s: str) -> bool:
        # processed_str = "".join([c.lower() for c in s if c.isalnum()])
        
        # l = 0
        # r = len(processed_str) - 1
        # while l <= r:
        #     if processed_str[l] != processed_str[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True

        l = 0
        r = len(s) - 1

        while l <= r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                print(s[l:r+1])
                print(l, r)
                return False
            l += 1
            r -= 1
        return True