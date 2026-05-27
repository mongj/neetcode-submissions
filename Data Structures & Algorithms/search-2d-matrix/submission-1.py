class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        n = rows * cols

        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l) // 2
            y = mid // cols
            x = mid % cols
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False