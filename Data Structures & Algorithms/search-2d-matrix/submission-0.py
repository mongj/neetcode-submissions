class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = l + (r - l) // 2
            row = matrix[mid]
            if target in row:
                l, r = 0, len(row) - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False
            elif target < row[0]:
                r = mid - 1
            else:
                l = mid + 1
        return False