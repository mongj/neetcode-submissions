class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_length = 0
        seen = set()

        while r < len(s):
            if s[r] in seen:
                # shift left pointer inwards until s[r] is out of the window
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            seen.add(s[r])
            max_length = max(r - l + 1, max_length)
            r += 1

        return max_length