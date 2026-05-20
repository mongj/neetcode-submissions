class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            prev = self.generate(numRows - 1)
            prev.append([1,1])
            return prev
        topRows = self.generate(numRows - 1)
        lastRow = topRows[-1]
        newRow = [1] * numRows
        for i in range(1, numRows - 1):
            newRow[i] = lastRow[i - 1] + lastRow[i]
        topRows.append(newRow)
        return topRows