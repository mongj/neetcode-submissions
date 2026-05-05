class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        most_freq_chars = []
        max_freq = float('-inf')
        for key, val in freq.items():
            if val > max_freq:
                max_freq = val
                most_freq_chars = [key]
            elif val == max_freq:
                most_freq_chars.append(key)

        print("most_freq_chars", most_freq_chars)

        acc = 0

        for c in s:
            l, r = 0, 0
            num_replacements = k
            while r < len(s):
                if s[r] == c:
                    r += 1
                elif num_replacements > 0:
                    num_replacements -= 1
                    r += 1
                else:
                    # move left pointer in until we get back one swap
                    while s[l] == c:
                        l += 1
                    l += 1
                    r += 1
                acc = max(acc, r - l)

        return acc

# s = XYYXYY k = 2
# 6

# s = ABCABCA k = 1
# 2