class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        writePtr = 0
        currChar = ''
        currCount = 0
        compLen = 0
        for i, char in enumerate(chars):
            if i > 0 and char != currChar:
                # write back first
                compStr = currChar
                if currCount > 1:
                    compStr += str(currCount)
                for c in compStr:
                    chars[writePtr] = c
                    writePtr += 1
                compLen += len(compStr)
                currCount = 0
            # update currChar and currCount
            currChar = char
            currCount += 1
        compStr = currChar
        if currCount > 1:
            compStr += str(currCount)
        for c in compStr:
            chars[writePtr] = c
            writePtr += 1
        compLen += len(compStr)
        return compLen
