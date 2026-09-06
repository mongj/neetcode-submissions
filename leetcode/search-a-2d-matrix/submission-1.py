class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        l, r = 0, n_rows * n_cols - 1
        while l <= r:
            mid = l + (r - l) // 2
            row_i = mid // n_cols
            col_i = mid % n_cols
            cell = matrix[row_i][col_i]
            if cell == target:
                return True
            elif cell > target:
                r = mid - 1
            else:
                l = mid + 1
        return False