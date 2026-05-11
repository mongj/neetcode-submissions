class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        writePtr = readPtr = 0
        while readPtr < n:
            chars[writePtr] = chars[readPtr]
            writePtr += 1

            # get length
            j = readPtr
            while j < n - 1 and chars[j + 1] == chars[j]:
                j += 1 
            count = j - readPtr + 1
            if count > 1:
                for c in str(count):
                    chars[writePtr] = c
                    writePtr += 1
            
            readPtr = j + 1
        return writePtr