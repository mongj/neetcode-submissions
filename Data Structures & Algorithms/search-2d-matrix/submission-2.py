class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        
        l, r = 0, r * c - 1
        while l <= r:
            mid = l + (r - l) // 2
            row, col = mid // c, mid % c
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
        