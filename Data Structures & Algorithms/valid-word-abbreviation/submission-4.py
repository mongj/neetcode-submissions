class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if abbr[j] == word[i]:
                    j += 1
                    i += 1
                    continue
                else:
                    return False
            else:
                count = ""
                while j < len(abbr) and abbr[j].isdigit():
                    count += abbr[j]
                    j += 1
                if count[0] == "0":
                    return False
                i += int(count)

        return i == len(word) and j == len(abbr)