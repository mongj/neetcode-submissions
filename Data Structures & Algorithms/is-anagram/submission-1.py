class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = [0] * 26
        for c in s:
            counter[ord(c) - 97] += 1
        for c in t:
            if counter[ord(c) - 97] > 0:
                counter[ord(c) - 97] -= 1
            else:
                return False
        return sum(counter) == 0