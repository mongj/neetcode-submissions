class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        acc = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                freq = {}
                for c in s[i:j]:
                    if c in freq:
                        freq[c] += 1
                    else:
                        freq[c] = 1
                if sum(freq.values()) - max(freq.values()) <= k:
                    acc = max(acc, sum(freq.values()))
        return acc
        # l, r = 0, 0
        # longest_ss = 0

        # while l < r:
            

        # return longest_ss

# s = XYYXYY k = 2
# 6