class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letterToWord = {}
        wordToLetter = {}

        words = s.split()
        if len(words) != len(pattern):
            return False

        for i in range(len(words)):
            l, w = pattern[i], words[i]
            if (l in letterToWord and letterToWord[l] != w) or (w in wordToLetter and wordToLetter[w] != l):
                return False
            letterToWord[l] = w
            wordToLetter[w] = l

        return True